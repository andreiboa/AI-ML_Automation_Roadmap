
#Varable for testing loops

for level in range(21):
    if level == 0:
        continue
    print("Level:", level)
    if level % 5 == 0:
        print("Boss Level:", level)

player_health = 100


while player_health >= 0:
    player_health -= 15
    if player_health < 0:
        print("Player Health:", 0)
    else:
        print("Player Health:", player_health)
    if player_health <= 0:
        print("Game Over!")