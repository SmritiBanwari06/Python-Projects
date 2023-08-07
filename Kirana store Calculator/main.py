sum = 0
while(True):
    userInput = input("Enter the price of  the item or q to quit: ")
    if(userInput!= 'q'):
        sum = sum + int(userInput)
        print(f"Your Total so far: {sum}")
    else:
        print(f"Total amount is {sum}. Thanks for shopping with us! Happy Shopping!!!")
        break
