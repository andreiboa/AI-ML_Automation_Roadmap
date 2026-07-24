

#For learning Sets in Python

favorite_games = {"CoC", "LoL", "DOTA 2", "CSGO", "Valorant"}

for game in favorite_games:
    print(f"Favorite Game: {game}")

favorite_games.add("Minecraft")
favorite_games.remove("DOTA 2")

for game in favorite_games:
    print(f"Updated Favorite Game: {game}")

owned_games = {"CoC", "Hogwarts Legacy", "Death Stranding", "Valorant", "Minecraft"}

wishlist = {"Cyberpunk 2077", "Elden Ring", "Hogwarts Legacy", "Valorant"}

print(f"Games in both sides: {owned_games & wishlist}")
print(f"Unique Games in both sets: {owned_games | wishlist}")
print(f"All Games in owned sets: {owned_games - wishlist}")

