
print("Enter the integer for the player to guess.")
answer = int(input())
print ("Enter your guess.")
guess = int
num_guesses = 0
while guess != answer:
    guess = int(input())
    num_guesses +=1
    if guess > answer:
        print("Too high - try again:")
    elif guess < answer:
        print("Too low - try again:")
    else:
        print("You guessed it in",num_guesses,"tries.")