import random

print("Welcome to cowbull!!")
name = input("Enter you name: ")
print("Hope you enjoy your stay !!",name)
def game():
    number=list(range(10)) #shuffling the code
    random.shuffle(number)
    return number
    # print(number)
# game()

def player():
    num1 = game()  #converting into list
    secret_num = []
    for i in range(4):
        secret_num.append(num1[i])
    return secret_num
    # print(secret_num)
# player()

def checking():
    cow=[]
    bull=[]
    num2=player()
    guess = 10
    while guess > 0:
        guess1 = int(input("             (example:[0,1,2,3]\nEnter one guessing no: "))
        position = int(input(" Enter the position of num: "))
        print("<3")
        
        if guess1 in num2:
            index = num2.index(guess1)
            if index == position:
                if guess1 not in bull:
                    bull.insert(index,guess1)
                    print("Bull", bull)
                else:
                    ("You already found",bull,"try other digit")
            else:
                cow.append(guess1)
                print("Cow, you can reuse this digit in different position", cow )
        if bull == num2:
            print(name,"Congartulation !!! You won")
            break
        
        guess-=1
        print(guess,"chances left")
    else:
        print("You lose")
        return bull
checking()


def play_again():
    while True:
        try_again = input("Enter yes to play again or no to exit")
        if try_again == "yes":
            checking()
        else:
            break
play_again()
        
    