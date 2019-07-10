# # exercise tracker 
#ask user for input on what action to take - walk or run
# print("Would you like to walk or run?")
# action = input().lower()




total_distance = 0
energy = 10

# while the user input gives a truthy, in this case action == walk or run
while True: 
    print("Would you like to walk or run?")
    action = input().lower()
    if action == "walk":
        total_distance += 1
        energy += 1 
        print("Distance from home is {}km.".format(total_distance) + " Energy level is {}.".format(energy))   
    elif action == "run": 
        if energy >= 3:
            total_distance += 5
            energy -= 2
            print("Distance from home is {}km.".format(total_distance) + " Energy level is {}.".format(energy))
        else: 
             print("You're too tired. Get some rest or have a snack.")
    elif action == "rest":
        energy += 1
        print("Great idea to take a breather.")
    elif action == "eat":
        energy += 3
        print("Yes! Get your energy up!")
    elif action == "go home": #allow the user to go home when done exercising
        print("Great break! Let's go home!")
        break 






