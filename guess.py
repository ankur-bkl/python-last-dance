secretWord="niu"
guess=""
guessCount=0
guessLimit=3
while guess!= secretWord and guessCount<guessLimit:
    guess=input("Enter the secret word: ")
    guessCount = guessCount +1
if guess==secretWord:
    print(f"Guessed the correct word in {guessCount} tries!")
else:
    print("You are out of guesses")
