
#Varables for testing Decision Making
player_health = 40
player_level = 12
has_key = False

if player_health <= 0:
    print("Game Over!")
elif player_health < 25:
    print("Low Health Warning")
else:
    print("Player is alive")

if player_level >= 10 and has_key:
    print("Dungeon Unlocked")
else:
    print("Dungeon Locked")