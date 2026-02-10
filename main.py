from fastmcp import FastMCP
import random
import json

#Server instance
mcp = FastMCP("Simple Calculator Server")

#Tools: Add numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number

    Returns:
        The Sum of a and b
    """
    return a+b

#Tools: Generate random numbers
@mcp.tool
def random_number(min_val: int=1, max_val: int=100) -> int:
    """Generate a random number within a range.
    Args:
        min_val: Minimum value (default: 1)
        max_val: Maximum value (default: 100)

    Returns:
        A random integer between min_val and max_val
    """
    return random.randint(min_val, max_val)

#Resource : Server Info
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""
    info = {
        "name": "Simple calculator server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }
    return json.dumps(info, indent=2)

#start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

