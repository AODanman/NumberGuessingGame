import random

importantNumber = random.randint(1, 100)
score = 100
counter = 0
gom = 'GAME OVER'
rnw = f'Right number was {importantNumber}'

while counter < 5:
    counter += 1
    usersGuess = int(input('Please enter your guess: '))
    if usersGuess == importantNumber:
        print('Congrulations')
        break
    if usersGuess > importantNumber:
        print('Smaller')
    else:
        print('Larger')
    score -= 20

if score > 0:
    print(f'Your score is {score}, and you got the number right at the {counter}. time')
else:
    print(gom.center(100, "-"))
    print(rnw.center(100, "-"))