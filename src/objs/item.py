#Inherits down to other types
class ItemBase:
    _id: int #Item reference id for items.json
    _rarity: int #raritys tbd
    _item_type: int # item type (0 armor, 1 mainhand, 2 offhand)
    _name: str #important
    _weight: float #might go unused will see
    _upgrade_level: int #for upgrade system, might change
    _stat_bonus: list #should be fed as (stat, bonus) lists in list , as in (strength, 2)

    def __init__(self, _new_id, _rarity_init, _name_init, _load_data=None):
        #ID is absolutely required for saving the item, mirror in item.JSON, init inherits down
        if not _new_id:
            raise ValueError("Needs ID or can not initialize item!")
        #needs loading from ID later        
        self._id = _new_id

        #default rest if not available - Replace with loading code later
        if _rarity_init:
            self._rarity = _rarity_init
        else:
            _rarity_init = 0

        if _name_init:
            self._name = _name_init
        else:
            self._name = "Item"

        #If we are loading a serialized item pass in the load data (Serialized)
        #Add deserialization when we have serialization

        self._item_type = 0

        if self._item_type == 0:
            self.load_data()



class Weapon(ItemBase):
    _damage: float
    _damage_type: int #0 for physical, 1 for magical
    _crit_chance: float #in %
    _crit_multi: float #as multiplier

    def load_data(self):
        pass

class Armor(ItemBase):
    _armour: float #as damage reduction % e.g. 0.25 = 25%
    _armour_type: int #0 for heavy, 1 for medium , 2 for light

    def load_data():
        pass

class OffHand(ItemBase):
    _offhand_armour: float #additional damage reistance as percent float, eg 0.25 = 25%
    _offhand_damage_mult: float #damage multiplier as multiplier e.g. 1.10 = 10% more