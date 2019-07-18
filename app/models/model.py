import random

strength = random.randint(8, 12)
defense = random.randint(8, 12)
speed = random.randint(8, 12)
max_health = random.randint(18, 24)

def stats(user_input):
    if user_input.lower() == "fast":
        return "Your strength: " + str(strength) + "\nYour defense: " + str(defense) + "\nYour speed: " + str(speed) + "\nYour max health: " + str(max_health)
    elif user_input.lower() == "strong":
        return "Your strength: " + str(strength) + "\nYour defense: " + str(defense) + "\nYour speed: " + str(speed) + "\nYour max health: " + str(max_health)
    elif user_input.lower() == "balance":
        return "Your strength: " + str(strength) + "\nYour defense: " + str(defense) + "\nYour speed: " + str(speed) + "\nYour max health: " + str(max_health)

