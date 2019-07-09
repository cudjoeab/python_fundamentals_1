# secret number 

secret_number = 155
guess = int(input())

if guess == secret_number:
    print("you win!")
elif (guess == secret_number + 1) or (guess == secret_number - 1):
    print("so close!")
else: 
    print("try again")