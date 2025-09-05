import os
import asyncio

from rv16_lib.logger import logger

from service import RegisterService

async def main():
    logger.info('Starting service')
    service = RegisterService()
    await service.register_service(
        provider="local",
        configuration={
            "hostname": os.getenv("PRJ_NAME"),
            "port": os.getenv("PORT"),
        }
    )
    logger.info("Service registration completed!")

if __name__ == "__main__":
    asyncio.run(main())