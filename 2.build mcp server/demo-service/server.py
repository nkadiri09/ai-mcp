from fastmcp import FastMCP
mcp = FastMCP("demo-service ")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
@mcp.tool
def farewell(name: str) -> str:
    return f"Goodbye, {name}!"

@mcp.tool
def add(a:int, b:int) -> int:
    print(f"Adding {a} and {b}")
    return a + b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")           