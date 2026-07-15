

#For understanding lists in Python
favorite_games = ["NBA2k", "LoL", "Valorant", "DOTA2", "CoC"]

for game in favorite_games:
    print(f"Favorite game: {game}")

print(f"First Game: {favorite_games[0]} \n",
      f"Last Game: {favorite_games[-1]} \n",
      f"Total Games: {len(favorite_games)} \n")

favorite_games.append('CSGO')
favorite_games.remove('DOTA2')
favorite_games[2] = "Minecraft"

for game in favorite_games:
    print(f"Updated Favorite games: {game}")