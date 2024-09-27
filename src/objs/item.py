#Inherits down to other types
class ItemBase:
    _id: int #Item reference id for items.json
    _rarity: int #raritys tbd
    _name: str #important
    _upgrade_level: int #for upgrade system, might change
    _equpped: bool #whether or not the item is currently equipped

    #base bonus and weight for random additions
    #total stat wieghts should add up to 10, 

    #primary melee stat
    _stat_str_base: int
    _stat_str_weight: int

    #primary physical ranged
    _stat_dex_base: int
    _stat_dex_weight: int

    #primary health stat
    _stat_con_base: int
    _stat_con_weight: int

    #primary healing stat (and mana)
    _stat_wis_base: int
    _stat_wis_weight: int

    #primary magic ranged
    _stat_int_base: int
    _stat_int_weight: int

    def __init__(self, _new_id, _rarity_init = 0, _name_init = "Item", _load_data=None):
        #ID is absolutely required for saving the item, mirror in item.JSON, init inherits down
        if not _new_id:
            raise ValueError("Needs ID or can not initialize item!")
        #needs loading from ID later        
        self._id = _new_id

class Weapon(ItemBase):
    _damage: float
    _damage_type: int #0 for physical, 1 for magical
    _crit_chance: float #in %
    _crit_multi: float #as multiplier

    def __init__(self, _new_id, _rarity_init=0, _name_init="Item", _load_data=None):
        super().__init__(_new_id, _rarity_init, _name_init, _load_data)

        #deserialize load data here
        


class Armor(ItemBase):
    _armour: float #as damage reduction % e.g. 0.25 = 25%
    _armour_type: int #0 for heavy, 1 for medium , 2 for light

    
    def __init__(self, _new_id, _rarity_init=0, _name_init="Item", _load_data=None):
        super().__init__(_new_id, _rarity_init, _name_init, _load_data)

        #deserialize load data here

class OffHand(ItemBase):
    _offhand_armour: float #additional damage reistance as percent float, eg 0.25 = 25%
    _offhand_damage_mult: float #damage multiplier as multiplier e.g. 1.10 = 10% more

    
    def __init__(self, _new_id, _rarity_init=0, _name_init="Item", _load_data=None):
        super().__init__(_new_id, _rarity_init, _name_init, _load_data)

        #deserialize load data here