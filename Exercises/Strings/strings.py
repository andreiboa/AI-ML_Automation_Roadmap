


#Learn Strings in Python
player_name = "Andrei"

print(f"Original Name: {player_name} \n"
      f"Uppercase Name: {player_name.upper()} \n"
      f"Lowercase Name: {player_name.lower()} \n"
      f"Length of Name: {len(player_name)}")


filename = "player_save.json"

print(f"Ends with .json: {filename.endswith('.json')}")
print(f"Starts with player: {filename.startswith('player')}")

hp = 100
damage = 35 

print(f"Player {player_name} has {hp} HP and deals {damage} damage.")
