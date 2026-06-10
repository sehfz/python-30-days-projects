import random
answer="y"
while answer.lower() in ["y", "yes"]:
    rn = random.randint(0,99)
    attempts=0
    while True:
        if attempts >= 10:
            print("GAME OVER  :(  answer is : %i" %rn)
            play_again=input("\nDo you want play again ? y/n ")
            if play_again.lower() in ["y","yes"]:
                attempts=0
                print("OK :) LET'S GO ")
                break
            else :
                exit()
        gn = int(input("\nenter your guess number : (0 , 99)"))
        attempts+=1
        if gn > 99:
            print("please enter your guess number in range 0 , 99 : ")
        elif gn < rn :
            print("\nThe random number is bigger than %i" %gn)
        elif gn > rn :
            print("\nThe random number is smaller than %i" %gn)
       
        elif    gn == rn:
            print("NICE ... YOU WIN after %i try " %attempts)
            answer= input("Do you want play again ? y/n \n")
            if answer.lower() in ["y", "yes"]:
                print("OK")
                break
            elif answer.lower() in ["n", "no"] :
                answer="n"
                print (" OK ... GOODBYE ")
                
    
            
    
