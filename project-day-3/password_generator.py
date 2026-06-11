import random
capital_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
characters="!@#$%^&*-=+"
while True:
    User_selection=""
    password=""
    lenght = int(input("enter lenght password : "))
    capital=input("\nDo you want capital letters in your password? y/n :  " )
    if capital.lower() in ["y","yes"]:
        User_selection+=capital_letters
    lowercase=input("\nDo you want lowercase letters in your password? y/n :  " )
    if lowercase.lower() in ["y","yes"]:
        User_selection+=lowercase_letters
    number=input("\nDo you want numbers in your password? y/n :  " )
    if number.lower() in ["y","yes"]:
        User_selection+=numbers
    character=input("\nDo you want characters in your password? y/n :  " )
    if character.lower() in ["y","yes"]:
        User_selection+=characters
    if User_selection=="":
        print("Error:  you must select at least one character type! ")
        continue
    for i in range(lenght):
        password+=random.choice(User_selection)
    print("\nyour generated password is: ", password)
    answer=input("\nDo you want any more ? y/n :  ")
    if answer.lower() in ["y","yes"]:
        continue
    else:
        break