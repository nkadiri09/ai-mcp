# python
from fastmcp import FastMCP
mcp = FastMCP("demo-service")

@mcp.tool(description="Return a friendly greeting for the given name.")
def greet(name: str) -> str:
    """Greet someone by name.

    Args:
        name: Person's name.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"

@mcp.tool(description="Return a farewell message for the given name.")
def farewell(name: str) -> str:
    """Say goodbye to someone.

    Args:
        name: Person's name.

    Returns:
        A farewell string.
    """
    return f"Goodbye, {name}!"

@mcp.tool(description="Add two integers and return the sum.")
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Sum of a and b.
    """
    print(f"Adding {a} and {b}")
    return a + b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
