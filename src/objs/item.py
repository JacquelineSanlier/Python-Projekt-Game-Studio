#Inherits down to other types
class ItemBase:
    _id: int #Item reference id for items.json
    _rarity: int #raritys tbd
    _name: str #important
    _upgrade_level: int #for upgrade system, might change
    _equpped: bool #whether or not the item is currently equipped

    #base bonus and weight for random additions

    #primary melee stat ID 1
    _stat_str_base: int
    _stat_str_weight: int

    #primary physical ranged ID 2
    _stat_dex_base: int
    _stat_dex_weight: int

    #primary health stat ID 3
    _stat_con_base: int
    _stat_con_weight: int

    #primary healing stat (and mana) ID 4
    _stat_wis_base: int
    _stat_wis_weight: int

    #primary magic ranged (and mana) ID 5
    _stat_int_base: int
    _stat_int_weight: int

    def __init__(self, _new_id, _rarity_init = 0, _name_init = "Item", _load_data=None):
        #ID is absolutely required for saving the item, mirror in item.JSON, init inherits down
        if not _new_id:
            raise ValueError("Needs ID or can not initialize item!")
        #needs loading from ID later        
        self._id = _new_id

        self._stat_str_weight = 0
        self._stat_dex_weight = 0
        self._stat_con_weight = 0
        self._stat_int_weight = 0
        self._stat_wis_weight = 0

    #quick get for total weights
    def get_weight_total(self) -> int:
        return self._stat_str_weight + self._stat_dex_weight + self._stat_con_weight + self._stat_wis_weight + self._stat_int_weight

    #takes a result from randomization and returns the id for the stat that resulted
    def get_statid_by_weight(self, _result: int) -> int:

        #ex a roll result of 2 for a sword with 5 0 5 weihting should add str
        #for the above _str_raange start will be 0, and _con_range_start will be 5
        _str_range_start = 0
        _dex_range_start = self._stat_str_weight
        _con_range_start = _dex_range_start + self._stat_dex_weight
        _wis_range_start = _con_range_start + self._stat_con_weight
        _int_range_start = _wis_range_start + self._stat_wis_weight
        _total = _int_range_start + self._stat_int_weight
        
        if _result in range(_str_range_start, _dex_range_start) :
            return 1 # id for str
        if _result in range(_dex_range_start, _con_range_start) :
            return 2 # id for dex
        if _result in range(_con_range_start, _wis_range_start) :
            return 3 # id for con
        if _result in range(_wis_range_start, _int_range_start) :
            return 4 # id for wis
        if _result in range(_int_range_start, _total) :
            return 5 # id for int
        
        return 0 #could not parse weight


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