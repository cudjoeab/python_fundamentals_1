# # exercise tracker 

total_distance = 0

#ask user for input on what action to take - walk or run
# print("Would you like to walk or run?")
# action = input().lower()

# while the user input gives a truthy, in this case action == walk or run
while True: 
    print("Would you like to walk or run?")
    action = input().lower()
    if action == "walk":
        total_distance += 1
        print("Distance from home is {}km.".format(total_distance))
    elif action == "run": 
        total_distance += 5
        print("Distance from home is {}km.".format(total_distance))
    elif action == "go home": #allow the user to go home when done exercising
        print("Great break! Let's go home!")
        break 
    
