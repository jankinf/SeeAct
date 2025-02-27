import asyncio
from seeact_package.seeact.agent import SeeActAgent
from dotenv import load_dotenv

load_dotenv()


async def run_agent():
    agent = SeeActAgent(config_path="src/config/demo_mode.toml")
    await agent.start()
    while not agent.complete_flag:
        prediction_dict = await agent.predict()
        await agent.execute(prediction_dict)
    await agent.stop()


if __name__ == "__main__":
    asyncio.run(run_agent())
