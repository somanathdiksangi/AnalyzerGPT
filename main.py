import asyncio
from team.analyzer_gpt_team import getDataAnalyzerTeam
from config.constants import MODEL
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from config.model_client import get_model_client
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage


async def main():
    model_client = get_model_client()
    docker = get_docker_executor()
    team = getDataAnalyzerTeam(docker, model_client)

    try:
        task = 'Can you give me a graph of number of people who survived and died in the titanic Dataset?'

        await start_docker_executor(docker)

        async for message in team.run_stream(task=task):
            print('='*40)
            if isinstance(message, TextMessage):
                msg = f"{message.source}: {message.content}"
                print(msg)
            elif isinstance(message, TaskResult):
                # Handle TaskResult differently - check available attributes
                msg = f"Task Result: {message}"
                if hasattr(message, 'summary'):
                    msg = f"Task Result Summary: {message.summary}"
                print(msg)
            print('='*40)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
    
    finally:
        await stop_docker_executor(docker)

if __name__ == '__main__':
    asyncio.run(main())