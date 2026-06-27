import asyncio

from agent import MCPAgent


async def main():

    agent = MCPAgent()

    await agent.initialize()

    while True:

        q = input("You: ")

        if q in ["exit", "quit"]:
            break

        answer = await agent.chat(q)

        print("\nAssistant:", answer, "\n")


if __name__ == "__main__":
    asyncio.run(main())