#Prove 08 - Kosei Hatakenaka
again = "y"
while again.lower() == "y":
    print("\nWelcome to the word guessing game!")
    print()


    secret = "mouse"
    count = 10
    guess = 0
    word = ""
    print("Your hint is ",end = "")
    for underscore in range(len(secret)):
        print("_ ", end = "")

    while word != secret: #check if word if word is not equal to secret. If it is, the loop will stop.
        print()
        print()
        print(f"You have {count} tries left.")
        word = input("What is your guess? ")
        count -= 1
        guess += 1
        if word != secret: #if word is equal to secret then it will skip the whole process and proceed to final output
            if len(word) == len(secret):
                print("Your hint is ",end = "")
                master = [ secret[index] for index in range(len(secret))]
                for index1 in range(len(word)): #index takes on a value of a number from the number of letter in "word"
                    letter_word = word[index1]
                    letter_secret = secret[index1]
                    if letter_word == letter_secret:
                        print(letter_word.upper() , end = "")
                    elif letter_word in master:
                        print(letter_word.lower(), end = "")
                    else:
                        print("_ " , end = "")
            else:
                print("Sorry, the guess must have the same number as the letter of the scecret word.", end="")
        if count == 0:
            break

    if count > 0:
        print("\nCongratulations! You guessed it!") #final output
        print(f"It took you {guess} guesses.") #final output
        again = "n"
    elif count == 0:
        print()
        print("\nGame over. You ran out of tries.") 
        print(f"It took you {guess} guesses.")
        print()
        again = input("Do you want to try again? y/n? ")



