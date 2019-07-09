# example of user input 
print("What is your name?")
user_name = input()
print("Hello, {}".format(user_name))

secret_password = "please"

print ("What's the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print ("That's {}!".format(correct_or_not))

#examples for integers
print("How many cookies have been eaten?")
eaten = input()

#convert user input to interger and subtract it from 12
remaining_cookies = 12 - int(eaten)

print ("There are {} cookies left.".format(remaining_cookies))

#Challenge, asking the user their age 
print ("In which year were you born?")
birth_year = int(input())

age = 2019 - birth_year

print("You are {} years old.".format(age))
