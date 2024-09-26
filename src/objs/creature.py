class CreatureBase:
    _id: int
    _health

    def __init__(self, _id: int, _name: str, _health: int, _attack_power: int, _max_HP: int):
        self._id = _id
        self.name = _name
        self.health = _health
        self.attack_power = _attack_power
        self.max_HP = _max_HP

    def get_id(self):
        return self._id

class Player(CreatureBase):
    
    def __init__(self, _name: str, _health: int, _attack_power: int, _max_HP: int):
        super().__init__(0, _name, _health, _attack_power, _max_HP)

    def take_damage(self, _damage: int):
        self.health -= _damage
        if self.health > self.max_HP:
            self.health = self.max_HP
        elif self.health <= 0:
            self.die()


# inventar, offhand, armoury