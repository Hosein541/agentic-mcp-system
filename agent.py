from google.genai import types
import json 
from gemini_client import GeminiClient
from client import MCPClient
from tool_converter import GeminiToolConverter
from planner_schema import Plan
from memory import Memory

class MCPAgent:

    def __init__(self):

        self.llm = GeminiClient()
        self.mcp = MCPClient()

        self.tools = None
        self.memory = Memory()

    async def initialize(self):

        await self.mcp.connect()

        mcp_tools = await self.mcp.list_tools()

        self.tools = GeminiToolConverter.convert(mcp_tools)

    def _extract_function_calls(self, response):

        calls = []

        try:
            parts = response.candidates[0].content.parts

            for part in parts:

                if hasattr(part, "function_call") and part.function_call:

                    calls.append(part.function_call)

        except Exception:
            pass

        return calls

    

    async def plan(self, user_input: str):

        prompt = f"""
    You are a planner for an AI agent.
# 
    Break the user request into a step-by-step plan.
# 
    You MUST output ONLY valid JSON.
# 
    Each step must be:
    - tool name
    - arguments
# 
    Available tools:
    {[t.name for t in self.tools[0].function_declarations]}
# 
    User request:
    {user_input}
# 
    Output format:
    {{
      "steps": [
        {{
          "tool": "tool_name",
          "args": {{
            "a": 1,
            "b": 2
          }}
        }}
      ]
    }}
    """
        response = self.llm.generate(
            messages=prompt,
            tools=None
        )

        # Gemini raw text
        raw = response.text


        return json.loads(raw)
    
    async def execute_plan(self, plan):

        results = []

        for step in plan["steps"]:

            tool_name = step["tool"]
            args = step["args"]

            result = await self.mcp.call_tool(
                tool_name,
                args
            )

            results.append({
                "step": step,
                "result": result
            })

        return results

    

    async def finalize(self, user_input, results):

        prompt = f"""
    You are a helpful assistant.

    User question:
    {user_input}

    Execution results:
    {results}

    Give final natural language answer.
    """

        response = self.llm.generate(
            messages=prompt,
            tools=None
        )

        return response.text


    
    async def chat(self, user_input: str):

        # 1. save user input
        self.memory.add_user(user_input)

        # 2. plan
        plan = await self.plan(self.memory.messages)

        # 3. execute
        results = await self.execute_plan(plan)

        # 4. finalize
        final_answer = await self.finalize(user_input, results)




        # 5. save assistant output
        self.memory.add_assistant(text=final_answer)

        return final_answer
        