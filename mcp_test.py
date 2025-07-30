import json
import uuid
import asyncio
from typing import Any, Callable, List
from pydantic import BaseModel

import mlflow
from mlflow.pyfunc import ResponsesAgent
from mlflow.types.responses import ResponsesAgentRequest, ResponsesAgentResponse

from databricks_mcp import DatabricksMCPClient
from databricks.sdk import WorkspaceClient
# This snippet below uses the Unity Catalog functions MCP server to expose built-in
# AI tools under `system.ai`, like the `system.ai.python_exec` code interpreter tool

# ── 1) CONFIG ────────────────────────────────────────────────────────────────
catalog = 'cindy_demo_catalog'
schema = 'movies'
LLM_ENDPOINT_NAME = "databricks-claude-3-7-sonnet"
SYSTEM_PROMPT = "You are a helpful movie assistant."
DATABRICKS_CLI_PROFILE = "e2-demo-field-eng-cindy"
assert (
  DATABRICKS_CLI_PROFILE != "e2-demo-field-eng-cindy",
  "Set DATABRICKS_CLI_PROFILE to your Databricks CLI profile name")

# Initialize workspace & host
ws = WorkspaceClient(profile=DATABRICKS_CLI_PROFILE)
host = ws.config.host

mcp_server_url = f"{host}/api/2.0/mcp/functions/system/ai"
def test_connect_to_server():
    mcp_client = DatabricksMCPClient(server_url=mcp_server_url, workspace_client=ws)
    tools = mcp_client.list_tools()

    print(
        f"Discovered tools {[t.name for t in tools]} "
        f"from MCP server {mcp_server_url}"
    )

    result = mcp_client.call_tool(
        "system__ai__python_exec", {"code": "print('Hello, world!')"}
    )
    print(
        f"Called system__ai__python_exec tool and got result "
        f"{result.content}"
    )


test_connect_to_server()