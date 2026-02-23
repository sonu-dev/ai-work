from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP(name="LocalAI", host="0.0.0.0", port=8080)

# Example tool: addition
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Example tool: greeting
@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Running MCP server on http://127.0.0.1:8080")
    # Use the streamable-http transport
    mcp.run(transport="streamable-http")