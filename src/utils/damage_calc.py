import pygame.font

# very basic damage calc, just health - damage for now

from src.objs.creature import CreatureBase

def calculate_damage(attacker : CreatureBase, defender : CreatureBase):
    start_time = pygame.time.get_ticks()
    if not hasattr(defender, '_armor'):                                 # check for defender armor
        defender._armor = 0
    hp = defender._health + defender._armor

    if not hasattr(attacker, '_item'):                                 # maybe later
        additional_damaage = 0
    else:
        additional_damaage += attacker._item._damage
    
    damage = attacker._attack_power + additional_damaage

    defender._health = hp - damage                        # set defender health / damage done

    final_damage = hp - defender._health

    pygame.font.init()                                                  # initialize for combat text
    combat_font = pygame.font.SysFont('Comic Sans MS', 25)                  # initialize font for combat text

    # red text for visibility, and its cool
    text_surface = combat_font.render(f'{attacker._name} did {final_damage} damage to {defender._name}, and has {defender._health} health left! ', False, (255, 0, 0))
    # Get the size of the text surface

    # Blit the text surface onto the main screen surface at the center position
    return text_surface, start_time