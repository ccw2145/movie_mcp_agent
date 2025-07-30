import os
from databricks.sdk import WorkspaceClient
from databricks import agents
import mlflow
from mlflow.models.resources import DatabricksFunction, DatabricksServingEndpoint, DatabricksVectorSearchIndex
from mcp_agent import LLM_ENDPOINT_NAME, MANAGED_MCP_SERVER_URLS, DATABRICKS_CLI_PROFILE
from databricks_mcp import DatabricksMCPClient

databricks_cli_profile = DATABRICKS_CLI_PROFILE
# Initialize workspace & host
ws = WorkspaceClient(profile=databricks_cli_profile)
host = ws.config.host
current_user = ws.current_user.me().user_name

# Configure MLflow and the Databricks SDK to use your Databricks CLI profile
mlflow.set_tracking_uri(f"databricks://{databricks_cli_profile}")
mlflow.set_registry_uri(f"databricks-uc://{databricks_cli_profile}")
mlflow.set_experiment(f"/Users/{current_user}/movie_mcp_agent")

## Log the agent defined in mcp_agent.py
# here = os.path.dirname(os.path.abspath())
# agent_script = os.path.join(here, "mcp_agent.py")
agent_script = "mcp_agent.py"
resources = [
    DatabricksServingEndpoint(endpoint_name=LLM_ENDPOINT_NAME),
    # DatabricksFunction("system.ai.python_exec"),
    # --- Uncomment and edit the following lines to include custom mcp servers hosted on Databricks Apps ---
    # DatabricksApp(app_name="app-name")
]

for mcp_server_url in MANAGED_MCP_SERVER_URLS:
    mcp_client = DatabricksMCPClient(server_url=mcp_server_url, workspace_client=ws)
    resources.extend(mcp_client.get_databricks_resources())

with mlflow.start_run():
    logged_model_info = mlflow.pyfunc.log_model(
        artifact_path="mcp_agent",
        python_model=agent_script,
        resources=resources,
    )
    
catalog = 'cindy_demo_catalog'
schema = 'movies'
UC_MODEL_NAME = f"{catalog}.{schema}.movie_mcp_agent"
registered_model = mlflow.register_model(logged_model_info.model_uri, UC_MODEL_NAME)

agents.deploy(
    model_name=UC_MODEL_NAME,
    model_version=registered_model.version,
)