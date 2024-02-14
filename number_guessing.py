import random

a = int(input('Enter lower bound: '))
b = int(input('Enter upper bound: '))

num = random.randint(a, b)
print('You have total of 10 chance to guess')
cnt = 1

while cnt <= 10:
    cnt = cnt+1
    guess = int(input('Guess number: '))
    if guess == num:
        print('Correct')
        break
    elif guess < num:
        print('Low')
    else:
        print('High')
