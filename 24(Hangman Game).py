word = "aryan"
guessed = ""
chances = 5

print("\nWelcome To Hangman Game\n")

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter

        else:
            display += "_"

    print("Word:", display,"\n")

    if display == word:
        print("You WIN!!!")
        break

    guess = input("Guess A Letter: ")
    guessed += guess

    if guess not in word:
        chances -= 1
        print("Wrong Guess\n")
        print("Chances Left:", chances, "\n")

if chances == 0:
    print("You Lost\n")
    print("Word Was:", word)
