# server.py
from mcp.server.fastmcp import FastMCP
import os
import requests

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return "ab"


@mcp.tool()
def forward_to_direct(chatId: str, message: str, email: str, realtime: bool = False) -> dict:
    """
    Sends a POST request to the /api/direct endpoint with the given data.
    """
    url = "https://deciding-pelican-overly.ngrok-free.app/api/direct"
    payload = {
        "chatId": chatId,
        "message": message,
        "email": email,
        "realtime": realtime
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=25)
        return {
            "status_code": response.status_code,
            "response": response.json()
        }
    except Exception as e:
        return {"error": str(e)}
# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport = "stdio")