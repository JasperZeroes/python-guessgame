import random
name=str(input("Enter your name:"))
print("Welcome", name, "to my revised Guess Game")
number_to_guess= random.randint(1,50)
count=1
guess=int(input("Enter a number between 1 and 50:"))
if guess==0:
    print("The number needed is", number_to_guess)
    guess=int(input("Enter a number between 1 and 50: "))
    count+=0
while guess!=number_to_guess:
    print("Oops! Wrong Number. Try again")
    if guess > number_to_guess:
        print("Your Guess is higher than the number_to_guess")
    else:
        print("Your Guess is lower than the number_to_guess")
    count+=1
    guess=int(input("Enter a number between 1 and 50: "))
    if count==4:
        print("You lose!!!")
        print("You have exceeded the maximum number of guesses")
        print("Game over")
        break
    
else:
    print("You Are Correct. Congratulations!!!")
    print("The number_to_guess is", number_to_guess)
    print("You made it in", count, "guess(es)")
