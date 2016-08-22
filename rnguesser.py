import random

guess = 0
count = [0, 0, 0]

while guess != 'exit':
    print('Generating random number...')
    rng = random.randint(1,9)
    guess = input('Guess a number between 1 and 9: ')
    diff = int(guess) - rng
    if diff == 0:
        print('You got it exactly right!')
        count[1] += 1
    elif diff > 0:
        print('You guessed too high.')
        count[2] += 1
    elif diff < 0:
        print('You guessed too low.')
        count[2] += 1
    else:
        print('You did not guess a number!')
        count[0] -= 1
    count[0] += 1
    print("Starting again. Type 'exit' to end the game.\n")

print('You guessed %d times.' % count[0])
print('%d of your guesses were wrong.' % count[2])
print('%d of your guesses were right.' % count[1])
print('Thank you for playing!')
