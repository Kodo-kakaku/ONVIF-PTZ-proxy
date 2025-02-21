import asyncio

class PtzService:
    @staticmethod
    async def move(x: float, y: float) -> None:
        tasks = []
        if x != 0:
            tasks.append(PtzService.move_x_motor(x))
        if y != 0:
            tasks.append(PtzService.move_y_motor(y))

        if tasks:
            await asyncio.gather(*tasks)

    @staticmethod
    async def move_x_motor(x: float) -> None:
        print(f"Move ptz platform on {x} degrees.")

    @staticmethod
    async def move_y_motor(y: float) -> None:
        print(f"Move ptz platform on {y} degrees.")
