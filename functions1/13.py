import random
def guesser(n, name):
    number = random.randint(1, 20)
    count = 1
    while n != number:
        if n < number:
            print('Your guess is too low.')
        elif n > number:
            print('Your guess is too high')
        n = int(input('Take a guess.\n'))
        count += 1
    print('Good job, %s! You guessed my number in %d guesses!' %(name, count))
    
    
    
name = input('Hello! What is your name?\n')
num = int(input('Well, %s, I am thinking of a number between 1 and 20.\nTake a guess.\n' % name))
guesser(num, name)
