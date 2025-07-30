# Movie MCP Agent

A conversational agent for movie data, leveraging Managed MCP servers for vector search and Unity Catalog functions. The agent auto-discovers tools from configured MCP endpoints and can be extended with custom tools.

Code adapted from Databricks MCP Documentation: https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp#deploy-your-agent  

See `mcp_agent.py` for configuration and extension details.

## Main Tools 
Using Databricks Managed MCP Server

**Vector Search Tool**
- Movie Overview Vector Seach Index: `cindy_demo_catalog__movies__overview_index`: Allow agent to search for movies based on descriptions or themes

**Unity Catalog Functions**
- Movie Economics Tool (`cindy_demo_catalog__movies__lookup_movie_economics`): Provides information about a movie's budget and revenue.
- Movie Rating Tool (`cindy_demo_catalog__movies__lookup_movie_rating`): Returns metadata about movies including movie's TMDB ID and certification/rating.

## Usage 
Follow instructions from  Databricks Documentation: https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp#build-an-agent-with-managed-mcp-servers
1. Set up local environment and install dependencies from `requirements.txt` in your local environment.
2. Run `driver.py` using Databricks Connect.

