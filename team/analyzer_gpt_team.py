from agents.data_analyzer_agent import getDataAnalyzerAgent
from agents.code_executor_agent import getCodeExecutorAgent
from autogen_agentchat.teams import RoundRobinGroupChat,SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.constants import TEXT_MENTION_TERMINATION


def getDataAnalyzerTeam(docker,model_client):
    code_executor_agent = getCodeExecutorAgent(docker)
    data_analyzer_agent = getDataAnalyzerAgent(model_client)

    team= RoundRobinGroupChat(
        participants=[data_analyzer_agent,code_executor_agent],
        max_turns=10,
        termination_condition=TextMentionTermination(TEXT_MENTION_TERMINATION)
    )
        
        
        

    return team

