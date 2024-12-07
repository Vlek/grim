"""
Grim's Game Engine
"""


class GameEngine:

    def __init__(self) -> None:
        self.player: Player = Player()
        self.rooms: list[Room] = []
