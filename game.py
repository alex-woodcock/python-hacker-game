import random

print("guess a random number between 1 and 2147483647! Its a different number every time! good luck!

def game():
    userInput = input('\nInput a math expression for your guess: ')
    if eval(userInput + "== random.randrange(2147483647)"):
        print("you win !")
    else:
        print("you lose loser")

while True:
    game()
    if (input("play again? y/n: ").lower()[0] == 'n'):
        break
