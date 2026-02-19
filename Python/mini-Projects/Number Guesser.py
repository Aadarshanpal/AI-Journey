import random
count = -1
number = random.randint(1,100)
print("The computer has randomly a number in the range 1-100, you got 10 tries.")
while True:
    count += 1
    if count == 10:
        print("You lose, its been 10 tries :(")
        break
    print("----------------------------------------------------------")
    guess = int(input("Enter your guess: "))
    if guess < 0 or guess > 100:
        print("Number not in rangee.\n")
        continue
    if guess < number:
        print("Go higher!\n")
    elif guess == number:
        print("You won! Congratulations!\nIt took you exactly",count,"tries!")
        break
    else:
        print("Go Lower!\n")
    