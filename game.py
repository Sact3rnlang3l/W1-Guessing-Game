import random

player_name = str(input("Well Howdy there Partner, What's your name? \n"))

guesses = 0

print('Well, ' + player_name+ ' I\'m thinkin of a number between 1 and 100, can you guess it? ') 

number = random.randint(1,100)

guess = int(input())


while guesses < 15:
        guess = int(input())
        guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            guesses = str(guesses)
            
            break
if guess == number:
    print('Well Howdy ' +player_name+ '! You got it in only ' +guesses+ ' tries!')
else:
    print('Darn, I ran outta time, try again later')
