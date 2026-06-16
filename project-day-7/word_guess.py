import random

words=["python", "programming", "front", "back", "code", "developer"]
secret_word=random.choice(words)
def show_word(secret_word, guessed_letters):
    display=""
    for letter in secret_word:
        if letter in guessed_letters:
            display+=letter+" "
        else:
            display+="_ "
    return display

guessed_letters=[]
attempts=0
max_attempts=6
while True:
    print("\n"+show_word(secret_word, guessed_letters))
    guess = input("Enter a letter : ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts+=1
        print("Wrong!!!%i attempts left. "%(max_attempts-attempts))
    
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\n You won!!! the word was: {secret_word}")
        break
    
    if attempts>=max_attempts:
        print(f"\n You lost!!! The word was: {secret_word}")
        break
    