class CreatureBase:
    _id: int
    _health: int
    _name: str
    _attack_power: int
    _max_HP: int

    def __init__(self, _id: int, _name: str, _health: int, _attack_power: int, _max_HP: int):
        self._id = _id
        self._name = _name
        self._health = _health
        self._attack_power = _attack_power
        self._max_HP = _max_HP

    def get_id(self):
        return self._id

class Player(CreatureBase):
    
    def __init__(self, _name: str, _health: int, _attack_power: int, _max_HP: int):
        super().__init__(0, _name, _health, _attack_power, _max_HP)

    def check_health(self):
        if self.health > self.max_HP:
            self.health = self.max_HP
        elif self.health <= 0:
            self.die()


# add space for inventary, offhand, armoury, main_hand