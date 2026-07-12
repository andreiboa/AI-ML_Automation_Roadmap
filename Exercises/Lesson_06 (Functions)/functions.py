


#for testing functons
def display_player_stats(name, health, damage):
    print("Player Name:", name, 
          "\nPlayer Health:", health, 
          "\nPlayer Damage:", damage,)

display_player_stats("Andrei", 100, 35)
display_player_stats("John", 100, 30)
display_player_stats("Jane", 100, 25)


#define a function to calculate critical hit damage
def calculate_critical_hit(critical_damage):
    return critical_damage * 2

critical_hit_damage = calculate_critical_hit(70)
print("Critical Hit Damage:", critical_hit_damage)
display_player_stats("Jane", 100, calculate_critical_hit(25))


#define a function to check if player can enter dungeon
def can_enter_dungeon(level, has_key):
    if level >= 10 and has_key:
        return True
    else:
        return False

print("Can enter dungeon:", can_enter_dungeon(12, True))