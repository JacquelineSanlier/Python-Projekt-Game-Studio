# honestly, still no idea what im doing

class DamageCalc:
    def __init__(self, _attacker, _defender):
        self._attacker = _attacker  # Attacker can be Player or CreatureBase
        self._defender = _defender  # Defender can be Player or CreatureBase

    def _calculate_attack_power(self):
        """Calculates the attack power based on the attacker."""
        if self._attacker._id == 0:  # If the attacker is the Player
            attack_power = self._attacker._attack_power
            if self._attacker.main_hand and self._attacker.main_hand._equipped:
                attack_power += self._attacker.main_hand._damage
        else:  # For creatures
            attack_power = self._attacker._attack_power
        return attack_power

    def _calculate_defense(self):
        """Calculates the defense value of the defender."""

        defense = 0
        # Check if the defender is the player
        if self._defender._id == 0:
            # If the player has armor and it's equipped, add armor defense
            if hasattr(self._defender, 'armor') and self._defender.armor and self._defender.armor._equipped:
                defense += self._defender.armor._armour  # Add armor defense if equipped
        # For creatures, defense remains 0 by default
        return defense

    def calculate_damage(self):
        """Calculates and returns the damage done and the defender's remaining health."""
        attack_power = self._calculate_attack_power()  # Get the attack power
        defense = self._calculate_defense()  # Get the defense value

        # Calculate the final damage dealt
        final_damage = max(0, attack_power - defense)  # Ensure damage is not negative
        
        # Update defender's health
        self._defender._health = max(0, self._defender._health - final_damage)  # Prevent health from going negative

        print(f'Attack Power: {attack_power}, Defense: {defense}, Damage Done: {final_damage}')

        # Return final damage dealt and remaining health of the defender
        return final_damage, self._defender._health