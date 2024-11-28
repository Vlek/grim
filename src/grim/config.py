from dataclasses import dataclass


@dataclass
class GrimConfig:
    disableMusic: bool
    musicVolume: int
    disableGameSounds: bool
    gameSoundVolume: int
