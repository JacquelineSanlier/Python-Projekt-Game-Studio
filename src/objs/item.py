#Inherits down to other types
class ItemBase:
    _id: int
    _rarity: int
    _name: str
    _weight: float
    _upgrade_level: int
    _stat_bonus: list

    def __init__(self, _new_id, _rarity, _name, _load_data):
        #ID is absolutely required for saving the item, mirror in item.JSON, init inherits down
        if not _new_id:
            raise ValueError("Needs ID or can not initialize item!")
        #needs loading from ID later        
        self._id = _new_id

        #default rest if not available
        if not self._rarity:
            self._rarity = _rarity
        else:
            _rarity = 0

        if not self._name:
            self._name = _name
        else:
            self._name = "Item"

        #If we are loading a serialized item pass in the load data (Serialized)
        #Add deserialization when we have serialization

class Weapon(ItemBase):
    _damage: float
    _damage_type: int
    _crit_chance: float
    _crit_multi: float

class Armor(ItemBase):
    _armour: float
    _armour_type: int

class OffHand(ItemBase):
    _offhand_armour: float
    _offhand_damage_mult: float