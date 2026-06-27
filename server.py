import math
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together. Use when user wants sum, total, or addition."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract second number from first. Use for difference or remainder calculations."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers. Use for product, scaling, or repeated addition."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide first number by second. Use for ratios or splitting values."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power of b. Use for exponentiation like x^y."""
    return a ** b


@mcp.tool()
def sqrt(x: float) -> float:
    """Return square root of a number."""
    return math.sqrt(x)


@mcp.tool()
def factorial(n: int) -> int:
    """Compute factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("negative not allowed")
    return math.factorial(n)


if __name__ == "__main__":
    mcp.run()