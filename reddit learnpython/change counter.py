def get_change_value():
    while True:
        price = input("Item Price: ")
        cash = input("Cash Given: ")
        if price > cash:
            print ("You sure about that? Looks like you don't have enough cash to cover it!")
            continue
        change = float(cash) - float(price)
        count_change(change)


        if process_again() is False:
            break
        
def process_again():
    while True:
        process = input("Process another transaction? ").lower()
        if process == "yes":
            return True
        if process == "no":
            print("Thanks for using the change counter!")
            return False
        else:
            print("Sorry, didn't quite understand that...")
            

def count_change(change):
    n = .05
    d = .10
    q = .25
    dol = 1
    nickels = 0
    dimes = 0
    quarters = 0
    dollars = 0
    while change / dol >=1:
        dollars += 1
        change -= dol
    while change / q >= 1:
        quarters += 1
        change -= q
    while change / d >= 1:
        dimes += 1
        change -= d
    while change / n >= 1:
        nickels += 1
        change -= n
    print("%d dollars \n%d quarters \n%d dimes \n%d nickels \n%d pennies" % (dollars,quarters,dimes,nickels,(change*100)))
    
            
            
        
