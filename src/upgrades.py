class WeaponUpgrade:
    def __init__(self, name, description, weapon_type, damage, cooldown, cost):
        self.name = name  # Name of the upgrade
        self.description = description  # Description of what the upgrade does
        self.weapon_type = weapon_type  # Type of weapon (e.g., "laser beam", "saw", "basic bullets")
        self.damage = damage  # Damage increase
        self.cooldown = cooldown  # Cooldown time reduction
        self.cost = cost  # Cost in points

    def __str__(self):
        return f"{self.name} ({self.weapon_type}): {self.description}\n" \
               f"Damage: {self.damage}, Cooldown: {self.cooldown}, Cost: {self.cost} points"


# Define your upgrades here
weapons_upgrades = [
    WeaponUpgrade(
        name="Laser Precision",
        description="Increases laser beam damage significantly.",
        weapon_type="laser beam",
        damage=15,     # Modify this value
        cooldown=1.0,  # Modify this value (in seconds)
        cost=20        # Modify this value
    ),
    WeaponUpgrade(
        name="Saw Blade Enhancement",
        description="Adds serrated edges to the saw for increased damage.",
        weapon_type="saw",
        damage=10,     # Modify this value
        cooldown=0.5,  # Modify this value (in seconds)
        cost=15        # Modify this value
    ),
    WeaponUpgrade(
        name="Bullet Speed Upgrade",
        description="Increases the speed of basic bullets for faster hits.",
        weapon_type="basic bullets",
        damage=5,      # Modify this value
        cooldown=0.2,  # Modify this value (in seconds)
        cost=10        # Modify this value
    ),
    WeaponUpgrade(
        name="Cooldown Reduction",
        description="Reduces cooldown time for all weapons.",
        weapon_type="all",
        damage=0,      # No damage increase
        cooldown=-0.3, # Reduces cooldown by 0.3 seconds
        cost=25        # Modify this value
    ),
    WeaponUpgrade(
        name="Explosive Rounds",
        description="Adds explosive damage to basic bullets.",
        weapon_type="basic bullets",
        damage=20,     # Modify this value
        cooldown=1.5,  # Modify this value (in seconds)
        cost=30        # Modify this value
    )
]

# Example of how to print all upgrades
for upgrade in weapons_upgrades:
    print(upgrade)
    print(upgrade.cost)