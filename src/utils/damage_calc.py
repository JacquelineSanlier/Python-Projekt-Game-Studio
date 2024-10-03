import pygame.font

# very basic damage calc, just health - damage for now

from src.objs.creature import CreatureBase

def calculate_damage(attacker: CreatureBase, defender: CreatureBase, combat_log: list):
    start_time = pygame.time.get_ticks()

    # Type checking
    if not isinstance(attacker, CreatureBase):
        attacker = CreatureBase(1, 'Default Attacker', 50, 1, 50)
    if not isinstance(defender, CreatureBase):
        defender = CreatureBase(1, 'Default Defender', 50, 1, 50)

    # Initialize combat log if not a list
    if not isinstance(combat_log, list):
        combat_log = []

    # Ensure defender has armor
    defender._armor = getattr(defender, '_armor', 0)

    # Calculate additional damage
    additional_damage = 0
    if hasattr(attacker, '_item'):
        additional_damage += attacker._item._damage

    # Calculate total damage
    damage = attacker._attack_power + additional_damage

    remaining_damage = damage

    # Reduce armor first
    if defender._armor > 0:
        armor_damage = min(defender._armor, remaining_damage)
        defender._armor -= armor_damage
        remaining_damage -= armor_damage

    # Reduce health with any remaining damage
    defender._health = max(0, defender._health - remaining_damage)

    final_damage = damage - (damage - remaining_damage)

    # Initialize font once at the start of your program
    combat_font = pygame.font.SysFont('Comic Sans MS', 25)

    # Create combat message
    if defender._health == 0:
        message = f'ONE HIT! {defender._name} defeated.'
    else:
        message = f'{final_damage} damage done! {defender._name} has {defender._health} health left.'

    text_surface = combat_font.render(message, False, (255, 0, 0))
    combat_log.append(message)

    return text_surface, start_time


def display_combat_log(display, combat_log, width, height):
    combat_font = pygame.font.SysFont('Comic Sans MS', 25)
    x = int(width * 0.55)
    y = int(height * 0.15)
    line_height = combat_font.get_height() + 5  # Add padding if needed

    last_messages = combat_log[-12:]  # This will get the last 12 messages

    for index, message in enumerate(last_messages):
        text_surface = combat_font.render(message, False, (0, 0, 0))
        display.blit(text_surface, (x, y + index * line_height))