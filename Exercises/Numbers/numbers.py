
#Test numbers in Python
player_health = 87
player_gold = 245
player_accuracy = 0.8765

print(f"Original accuracy: {player_accuracy} \n"
      f"Rounded accuracy: {round(player_accuracy, 2)} \n"
      f"Highest among the 3: {max(player_health, player_gold, player_accuracy)} \n"
      f"Lowest among the 3: {min(player_health, player_gold, player_accuracy)} \n"
      )

damage = -35
print(f"Absolute damage: {abs(damage)}")

score = "98"
score = int(score)
print(f"Score: {score}")
print(type(score))
