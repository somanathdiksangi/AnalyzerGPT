from autogen_agentchat.teams import RoundRobinGroupChat
from agent.code_executor import get_code_executor_agent
from agent.data_analyzer_agent import get_data_analyzer_agent
from autogen_agentchat.conditions import TextMentionTermination


def get_analyzer_team(docker,model_clind):
    code_executor_agent=get_code_executor_agent(docker)
    data_analyzer_agent=get_data_analyzer_agent(model_clind)
    condition=TextMentionTermination("STOP")

    team=RoundRobinGroupChat(
        participants=[data_analyzer_agent,code_executor_agent],
        termination_condition=condition,
        max_turns=10
    )
    return team