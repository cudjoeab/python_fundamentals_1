# # exercise tracker 

# total_distance = 0

# print("Would you like to walk or run?")
# action = input().lower()

# while total_distance < 12: 
#     if action == "walk":
#         total_distance += 1
#         print("Distance from home is {}km.".format(total_distance))
#     elif action == "run": 
#         total_distance += 5
#         print("Distance from home is {}km.".format(total_distance))
#     else: 


total_distance = 0

print("Would you like to walk or run?")
action = input().lower()

while total_distance < 20:
    print("Distance from home is {} km.".format(total_distance))
    total_distance += 1
    if action == "walk":
        total_distance += 1
        print("Distance from home is {}km.".format(total_distance))
        break 
    elif action == "run": 
        total_distance += 5
        print("Distance from home is {}km.".format(total_distance))
        break 
    
