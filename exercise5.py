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
             print("Energy level is {}.".format(energy) + "Get some rest or have a snack.")
    elif action == "sprint":
        if energy >= 5:
            total_distance +=8
            energy -= 5
            print("Wow you're fast! " + "Distance is {} km. ".format(total_distance) + "Energy level is {}.".format(energy))
        else: 
            print("Can't speed up right now... " + "Energy level is {}.".format(energy))
    elif action == "rest":
        energy += 1
        print("Great idea to take a breather." + "Energy level is {}.".format(energy))
    elif (action == "eat") or (action == "snack"): 
        energy += 3
        print("Yes! Get your energy up!" + "Energy level is {}.".format(energy))
    elif action == "go home": #allow the user to go home when done exercising
        print("Great break! Let's go home!")
        break 
    else: 
        print ("Your options are: go home\twalk\trun\tsprint\trest\teat or snack\t")
        






