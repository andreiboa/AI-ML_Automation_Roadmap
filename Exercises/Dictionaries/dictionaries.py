


#For underestanding Dicttionaries in Python
player = {
    "name": "Andrei",
    "health": 100,
    "damage": 35,
    "level": 5
}

print(f"Player Name: {player['name']} \n"
      f"Player Health: {player['health']} \n"
        f"Player Damage: {player['damage']} \n"
        f"Player Level: {player['level']} \n")

player["health"] = player["health"] - 20
player["gold"] = 500

for  key, value in player.items():
    print(f"Updated {key}: {value}")

enemy = {
    "name": "Goblin",
    "health": 80,
    "damage": 25
}

for key, value in enemy.items():
    print(f"{key}: {value}")