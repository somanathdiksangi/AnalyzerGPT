import asyncio
from team.analyzer_gpt_team import get_analyzer_team
from config.constant import MODEL
from config.docker_utils import get_docker_executor
from config.docker_utils import start_docker_executor
from config.docker_utils import stop_docker_executor
from agent.code_executor import get_code_executor_agent
from agent.data_analyzer_agent import get_data_analyzer_agent
from config.model_clind import get_model_client
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

async def main():
    model_clind=get_model_client()
    docker=get_docker_executor()
    team=get_analyzer_team(docker,model_clind)

    try:
        task="can you give me a graph of number os people who survived and died in the titanic dataset?"
        await start_docker_executor()
        async for messages in team.run_stream(task=task):
            print(messages)
            print('='*20)
            if isinstance(messages,TextMessage):
                print(msg:=f" {messages.source}: {messages.content}")
            elif isinstance(messages,TaskResult):
                print(msg:=f"Task Result: {messages.result}")
            print("="*40)

    except Exception as e:
        print(e)
    finally:
        await start_docker_executor()

        

if(__name__ == '__main__'):
    asyncio.run(main())
