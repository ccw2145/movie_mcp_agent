# Movie MCP Agent

A Databricks-based conversational agent for movie data, leveraging Managed MCP servers for vector search and Unity Catalog functions. The agent auto-discovers tools from configured MCP endpoints and can be extended with custom tools.

## Main Tools (examples)
- **vector_search_movies**: Find movies similar to a given title using vector similarity search.
- **search_movie_metadata**: Retrieve metadata for movies based on search criteria.
- **uc_list_movies**: List all movies in the Unity Catalog schema.
- **uc_get_movie_details**: Get detailed information for a specific movie from Unity Catalog.
- **Custom Tools**: Add your own MCP server URLs in `mcp_agent.py` to expose additional tools.

> Note: The actual tool names and descriptions are auto-discovered from your Databricks MCP servers and may vary depending on your configuration.

## Usage
1. Install dependencies from `requirements.txt` in your Conda environment.
2. Run the agent in a notebook or script. It will connect to Databricks, discover tools, and handle user queries.

See `mcp_agent.py` for configuration and extension details.
