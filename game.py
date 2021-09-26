import random

print("guess a random number between 1 and 2147483647! Its a different number every time! good luck!")
print("itd take a 5up3r l33t h4ck3r to crack this code, and im not even sure you were banned from the internet when you were 11")

while True:
    userInput = input('\nInput a math expression for your guess: ')
    solution = random.randrange(2147483647)
    if eval(userInput + " == "+str(solution)):
        print("what?? how did you do that??? you win!?!? my evil scheeeeeeeemeeeesssss!!!!")
        break
    else:
        print("hah, nice try but you were way off, you guessed "+str(eval(userInput))+" and the answer was "+str(solution))

##i was away for the start of the event but
##it looked like fun so i thought id make something
