class CreatureBase:
    _id: int

    def __init__(self, _id: int):
        self._id = id

    def get_id(self):
        return self._id

        class Player(CreatureBase):
    def __init__(self, _name: str, _health: int, _attack_power: int, _class: int):
        super().__init__(0)
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, _damage: int):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print(f"{self.name} has been defeated.")

    def heal(self, _amount: int):
        self.health += amount
        print(f"{self.name} has been healed by {amount} points.")    