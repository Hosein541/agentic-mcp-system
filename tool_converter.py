from google.genai import types


class GeminiToolConverter:

    @staticmethod
    def convert(mcp_tools):

        declarations = []

        for tool in mcp_tools.tools:

            declarations.append(

                types.FunctionDeclaration(

                    name=tool.name,

                    description=tool.description,

                    parameters_json_schema=tool.inputSchema
                )

            )

        return [

            types.Tool(

                function_declarations=declarations

            )

        ]