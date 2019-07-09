# Ask the user to enter their age, and then display a message telling them how many years apart in age you are from them. If they enter a number larger than 105, print "I'm not sure I believe you".

print("How old are you?")
user_age = int(input())
my_age = 27

# defining a conditional to change calculation
# if user_age < my_age: 
#     age_difference = my_age - user_age
# else:
#     age_difference = user_age - my_age

#cleaned up and simplified code
if user_age < my_age:
    age_difference = my_age - user_age
    print("I am {} years older than you.".format(age_difference))
elif user_age == my_age:
    print("Yay for 92 babies!")
else:
    age_difference = user_age - my_age
    print("I am {} years younger than you.".format(age_difference))

