from autogen_agentchat.agents import AssistantAgent
from agent.prompt.data_analyzer_agent import DATA_ANALYZER_PROMPT


def get_data_analyzer_agent(model_clind):
    """
    Returns an instance of the DataAnalyzerAgent configured to analyze data.

    Returns:
        AssistantAgent: Configured data analyzer agent.
    """
    
    data_analyzer_agent = AssistantAgent(
        name='DataAnalyzerAgent',
        model_client=model_clind
        description="An agent that analyzes data and provides insights.",
        system_message=DATA_ANALYZER_PROMPT
    )
    
    return data_analyzer_agent