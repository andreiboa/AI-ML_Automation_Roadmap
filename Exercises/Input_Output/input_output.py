

#For learning I/O in Python

name = input("Please enter your name: ")
favorite_game = input("Please enter your favorite game: ")

print(f"Hello {name}!\n\n"
       f"Your favorite game is {favorite_game}.")

hp = int(input("Please enter your health points: "))
damage = int(input("Please enter your damage points: "))

print(f"HP: {hp}\n"
        f"after taking one hit: {hp - damage}")

level = int(input("Please enter your level: "))

if level >= 10:
    print(f"Dungon unlocked")
else:
    print(f"Dungon locked, increase level to atleast 10")
