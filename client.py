from mcp import ClientSession
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:

    def __init__(self):

        self.server = StdioServerParameters(
            command="python",
            args=["server.py"]
        )

        self.session = None
        self.transport = None

    async def connect(self):

        self.transport = stdio_client(self.server)

        read, write = await self.transport.__aenter__()

        self.session = ClientSession(
            read,
            write
        )

        await self.session.__aenter__()

        await self.session.initialize()

    async def disconnect(self):

        if self.session:
            await self.session.__aexit__(
                None,
                None,
                None
            )

        if self.transport:
            await self.transport.__aexit__(
                None,
                None,
                None
            )

    async def list_tools(self):

        return await self.session.list_tools()

    async def call_tool(
        self,
        name,
        arguments
    ):

        return await self.session.call_tool(
            name,
            arguments
        )