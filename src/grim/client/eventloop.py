import asyncio

import rich

logo: str = r"""
  ________       __         
 /  _____/______|__| _____  
/   \  __\_  __ \  |/     \ 
\    \_\  \  | \/  |  Y Y  \
 \______  /__|  |__|__|_|  /
        \/               \/ 
"""


async def main():
    rich.print(logo)
    await asyncio.sleep(10)


class EventLoop:

    def __init__(self) -> None: ...

    def run(self) -> None:
        asyncio.run(main())
