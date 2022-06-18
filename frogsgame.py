def demonstrate(initialList, finalList): #global function
    #this function is declared to demostrate the rules of this game
    print("Initial List is: ",initialList)
    print("Desired List is: ",finalList)
    print("Instructions:")
    print("1. You can only move Frogs towards right and Toads towards left")
    print("2. A Frog/Toad can only move to next/previous position if empty or can jump over one Frog/Toad if the next position is empty")
    print("For instance, in initial list, the Frog at position 1 can't move but frog at position 2 can jump over frog at position 3 and come on position 4. Similarly, in initial list, the frog at position 3 can only move on position 4")
    print("3. Firstly you will choose whether you want to move a Frog or a Toad")
    print("4. Then you will give from and to position where from means from which place do you want to move a Frog/Toad and to means to which place do you want to move it")
    print("5. If the jump is allowed, the list will be updated and you will be displayed the updated list")
    print("6. If the jump is not allowed then the error will be displayed")
    print("7. You will win if you change the list to the desired list successfully")
    print("8. You can reset or exit the game at any point")
    print("9. Try to do in minimum number of moves")

def finalCondition(initialList, finalList): #global function
    #this function is used to check whether the final condition is reached or not
    #there is a loop running which will traverse the whole array and will compare it with the final desired array
    i = 0
    while i < 7:
        if initialList[i] != finalList[i]:
            return True
        else:
            ++i
    return False

def compareLists(initialList, finalList): #global function
    #this function is used to check whether the lists are equal or not
    #there is a loop running which will traverse the whole array and will compare it with the second array
    i = 0
    while i < 7:
        if initialList[i] != finalList[i]:
            return False
        else:
            ++i
    return True

def moveFrog(f, t, initialList): #global function
    #this function is declared to move the frog
    #it check all the impossible moves if the move clears all the conditions then it is a true move and the frog is moved
    if f < 1 or f > 7 or t < 1 or t > 7:
        print("Invalid positions. Only select between 1 to 7")
    elif f > t:
        print("Frog can not move backward")
    elif initialList[t - 1] != "":
        print("Desired position is not empty")
    elif (t - f) > 2:
        print("Frog can only jump over one Frog/Toad")
    else:
        temp = initialList[f - 1]
        initialList[f - 1] = initialList[t - 1]
        initialList[t - 1] = temp

def moveToad(f, t, initialList): #global function
    #this function is declared to move the toad
    #it check all the impossible moves if the move clears all the conditions then it is a true move and the toad is moved
    if f < 1 or f > 7 or t < 1 or t > 7:
        print("Invalid positions. Only select between 1 to 7")
    elif t > f:
        print("Toad can not move forward")
    elif initialList[t - 1] != "":
        print("Desired position is not empty")
    elif (f - t) > 2:
        print("Toad can only jump over one Frog/Toad")
    else:
        temp = initialList[t - 1]
        initialList[t - 1] = initialList[f - 1]
        initialList[f - 1] = temp

def play(initialList, finalList): #global function
    #this function is used to play the game
    #once this function is invoked it will run until the final condition is arrived
    print("Current List : ",initialList)
    while finalCondition(initialList, finalList):
        print("[1] : Move Frog [2] : Move Toad [3] : Reset [0] : Exit")
        ch = int(input("Select an option : "))
        if ch == 1:
            f = int(input("From : "))
            t = int(input("To : "))
            moveFrog(f,t,initialList)
            print("Current List : ",initialList)
        elif ch == 2:
            f = int(input("From : "))
            t = int(input("To : "))
            moveToad(f,t,initialList)
            print("Current List : ",initialList)
        elif ch == 3:
            initialList.clear()
            initialList = ["Frog","Frog","Frog","","Toad","Toad","Toad"]
            print("Current List : ",initialList)
        else:
            break
    if compareLists(initialList, finalList):
        initialList = ["Frog","Frog","Frog","","Toad","Toad","Toad"]
        print("You Won")

print("Frogs and Toads Game")
print("Initial Positions:")
iList = ["Frog","Frog","Frog","","Toad","Toad","Toad"]
print(iList)
fList = ["Toad","Toad","Toad","","Frog","Frog","Frog"]
print("Desired Positions:")
print(fList)

#main menu at the start and calling relative functions
while True:
    print("[1] : Demonstrate Game [2] : Play Game [0] : Exit")
    choice = int(input("Select an option : "))
    if choice == 1:
        demonstrate(iList, fList)
    elif choice == 2:
        play(iList,fList)
    elif choice == 0:
        exit()
    else:
        print("Please select a relevant option")