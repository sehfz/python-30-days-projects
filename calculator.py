while True:
    first_number = float(input("Enter your first number : "))
    o = input("\nenter your operation ( * , +, -, / ) : ")
    if o!= "/":
        second_number = float(input("\nenter your second number : "))

    if o == "+" :
        rus=first_number+second_number
    elif o=="-":
        rus=first_number-second_number
    elif o=="*":
        rus = first_number*second_number
    elif o== "/":
        while True:
            second_number = float(input("\nenter your second number : "))
            if second_number==0:
                print("Erron, your second number is 0 ")
                
            else:
                rus=first_number/second_number
                break
    else:
        print("Error")
        exit()

    print (first_number , o , second_number, "= ", rus )
    ans=input("\n do you want try again ? y/n  ")
    if ans=="n" or ans=="N"or ans== "no":
        print("Goodbye")
        break

