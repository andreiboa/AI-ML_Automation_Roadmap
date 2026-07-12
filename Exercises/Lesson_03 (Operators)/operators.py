


#Variable for testng expressions
player_health = 80
player_damage = 15
enemy_health = 100

print("Health:",player_health, 
      "Damage:",player_damage, 
      "Enemy Health:",enemy_health)

print("After 1 Hit:", enemy_health - player_damage,
      "After 3 Hits:", enemy_health - (player_damage * 3),
      "Crit Hits:", player_damage * 2)


#Variable for testng operators
player_level = 8
has_key = True
gold = 250


print("Is player lvl 10 above?:",player_level >= 10,
        "\nIs player gold 20 above?:", gold >= 200,
        "\nIs player lvl 10 above and has key?:", player_level >= 10 and has_key,
        "\nIs player lvl 10 above or has key?:", player_level >= 10 or has_key,
        "\nPlayer does not have key?:", not has_key)