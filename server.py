from fastmcp import FastMCP

mcp = FastMCP("arithmetic-server")


@mcp.tool
def add(a: float, b: float) -> dict:
    """Add two numbers."""
    return {"result": a + b}


@mcp.tool
def subtract(a: float, b: float) -> dict:
    """Subtract the second number from the first."""
    return {"result": a - b}


@mcp.tool
def multiply(a: float, b: float) -> dict:
    """Multiply two numbers."""
    return {"result": a * b}


@mcp.tool
def divide(a: float, b: float) -> dict:
    """Divide the first number by the second."""
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}


if __name__ == "__main__":
    mcp.run(show_banner=False)
