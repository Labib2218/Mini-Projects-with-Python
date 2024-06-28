import random

permission = input("Do you want to start? [y/n] ").lower()
if permission == "y":
    while True:
        roll = input("Want to roll? [r/e]").lower()
        if roll == "r":
            print(random.randint(1, 6))
        else:
            print("Game Over")
            break

else:
    print("Try Again")
    quit()
