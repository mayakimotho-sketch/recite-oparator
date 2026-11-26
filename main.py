print("A recite oparator")
name=input("Enter your name:")
total=0
items=0
while True:
    print("Items available")
    print("1.1kg of sugar")
    print("2.soap")
    print("3.bread")
    print("4.1packet of milk")
    print("5.Close menu")
    number=int(input("Enter your number"))
    if number==1:
        good="Sugar"
        price=50
    elif number==2:
        good="Soap"
        price=20
    elif number==3:
        good="Bread"
        price=70
    elif number==4:
        good="Milk"
        price=40
    elif number==5:
        print("Thanks for shopping with us")
        break
    else:
        print("Invalid option please select the options above")
        continue
    quantity=int(input("Enter quantity"))
    cost=price*quantity
    total+=cost
    items+=quantity
    print(good," has been added to your cart")
    print("This is your total",total)
payment=float(input("Enter the amount to pay"))
if payment>total:
    change=payment-total
    print("Here is your change",change)
for i in range(30):
    print("-",end="")
print("Recite details")
print("The oparator:",name)
print("Here is your total:",total)
print("Here is the number of items:",items)
print("Here is the total amount:",payment)
print("Here is the change:",change)
