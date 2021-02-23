import random
num = random.randint(1,10)
print(num)
guess = []
count = 0
game = True
while num != guess and count < 3 and game == True:
    guess = input("Guess my number between 1 and 10: ")
    guess = int(guess)
    if guess == num:
        count += 1
        count = str(count)
        print("You did it in " + count + " trie(s) :) Congrats.")
        count = int(count)
        again = input("Play again? y/n: ")
        if again == 'y':
            game == True
            num = random.randint(1,10)
            guess = []
            count = 0
        else:
            game == False
    else:
        count += 1
        count = str(count)
        print("You didn't get it right. You have guessed " + count + "/3 guesses.")
        count = int(count)
        if count == 3:
            count = str(count)
            print("You tried " + count + " times and couldn't guess it. Sorry :(")
            count = int(count)  
            again = input("Play again? y/n: ")
            if again == 'y':
                game == True
                num = random.randint(1,10)
                guess = []
                count = 0
            else:
                game == False
print("Thanks for playing :)")
