import asyncio
from fastmcp import Client, FastMCP

async def main():
    async with  Client("http://127.0.0.1:8000/mcp") as client:
        if client.is_connected():
            print("connected to server")

        tools = await client.list_tools()
        print("available tools:", tools)
        for tool in tools:
            print(f"{tool.name}: {tool.description}")


if __name__ == "__main__":
    asyncio.run(main())