while True:
    score=0
    Capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    symbols="!@#$%^&*()"
    number="1234567890"
    password=input("Enter your password :\n ")
    if len(password)>=8:
        score+=1
    for ch in password:
        if ch in Capital:
            score+=1
            break
    for ch in password:
        if ch in lowercase:
            score+=1
            break
    for ch in password:
        if ch in symbols:
            score+=1
            break
    for ch in password:
        if ch in number:
            score+=1
            break
    print(score)

    if len(password) <8:
        print("\nUse at least 8 characters")
    if not any(ch in Capital for ch in password ):
        print("\nAdd uppercase letters (A-Z)")
    if not any(ch in lowercase for ch in password):
        print("\nAdd lowercase letters (a-z)")
    if not any(ch in symbols for ch in password):
        print("\nAdd symbols (!@#$%^&*()")
    if not any(ch in number for ch in password):
        print("\nAdd numbers (0-9)")
    if score ==5:
        print("\nThat's a strong password!")
    elif score==4 or score==3:
        print("\nThat's a normal password.")
    elif score < 3 :
        print("\nThat's a weak password.")
    again=input("\n Do you want to check another password? (y/n):")
    if again.lower() in ["y" , "yes"] :
        continue
    else:
        break






        

