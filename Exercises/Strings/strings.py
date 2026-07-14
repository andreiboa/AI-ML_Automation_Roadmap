


#Learn Strings in Python
player_name = "Andrei"

print(f"Original Name: {player_name} \nUppercase Name: {player_name.upper()} \nLowercase Name: {player_name.lower()} \nLength of Name: {len(player_name)}")


filename = "player_save.json"

if (filename.endswith(".json") or filename.startswith("player")):
    print("File is a JSON file")

hp = 100
damage = 35 

print(f"Player {player_name} has {hp} HP and deals {damage} damage.")
