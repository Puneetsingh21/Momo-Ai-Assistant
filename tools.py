import logging
from livekit.agents import function_tool, RunContext
from langchain_community.tools import DuckDuckGoSearchRun


@function_tool
async def search_web(
    context: RunContext,
    query: str) -> str:
    """
    Search the web using DuckDuckGo
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        logging.info(f"Web search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error occurred while searching the web: {e}")
        return "Error occurred while searching the web for '{query}'."




