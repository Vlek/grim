class BaseMob:
    base_hitpoints: int = 30
    base_stamina: int = 20

    def __init__(self) -> None:
        self.strength = 1
        self.dexterity = 1

        self.hitpoints_max = self.calcHitpointsMax()
        self.hitpoints = self.hitpoints_max

        self.stamina_max = 1
        self.stamina = self.stamina_max

    def calcHitpointsMax(self) -> int:
        return BaseMob.base_hitpoints + self.strength * 2

    def calcStaminaMax(self) -> int:
        return BaseMob.base_stamina + self.dexterity * 1
