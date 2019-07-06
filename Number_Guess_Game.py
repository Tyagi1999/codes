import random
print(" *** GUESS THE NUMBER. ***")
print("_______________________________________________________________________________")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def Play():
    x=random.randint(0,100)
    attempts=11
    for i in range(0,11):
        if i==10:
            print("\nSorry you lost the game. The correct number is: "+str(x))
            break
        attempts=attempts-1  
        print("\nYou have now "+str(attempts)+" chances.")  
        n=int(input("\nEnter any number between 0 and 100: "))
        if n==x:
            print("\nCongrats!! You are right.")
            break
        elif n<x:
            print("\nGuess higher number.")
            continue
        else:
            print("\nGuess lower number.")
            continue
    ch=input("\nPress P to play and Q to quit.\n")
    if ch=='p' or ch=='P':
        print("________________________________________________________________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        Play()
    if ch=='Q' or ch=='q':
        exit
Play()

    


