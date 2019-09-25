def get_weights():
    while True:
        print("Please select the unit of weight for your coins: ")
        print("1: Grams")
        print("2: Pounds")
        weight_decide = input()
        if weight_decide == "1" or weight_decide == "2":
            break
        else:
            print("Sorry, please type only 1 or 2.")
    
    print("Now please type the weight of each coin you have.")
    pen = float(input("Pennies: "))
    nic = float(input("Nickels: "))
    dim = float(input("Dimes: "))
    quarters = float(input("Quarters: "))
    if weight_decide == "2":
        pen,nic,dim,quarters = pound_to_gram(pen, nic, dim, quarters)
    coinwrap_estimator(pen,nic,dim,quarters)

def pound_to_gram(a,b,c,d):
    gpp = 453.592
    a = a*gpp
    b = b*gpp
    c = c*gpp
    d = d*gpp
    return a, b, c, d

def coinwrap_estimator(a,b,c,d):
    #define the weights of each coin
    cent = 2.5
    nickel = 5.0
    dime = 2.268
    quarter = 5.670
    #define how many fit into a wrap
    wr_cent = 50
    wr_nickel = 40
    wr_dime = 50
    wr_quarter = 40
    #find the number of coins based on input
    n_cent = a/cent
    n_nickel = b/nickel
    n_dime = c/dime
    n_quarter = d/quarter
    #finally, find the number of wrapper based on number of coins
    numwrap_c = round(1/(wr_cent/n_cent))
    numwrap_n = round(1/(wr_nickel/n_nickel))
    numwrap_d = round(1/(wr_dime/n_dime))
    numwrap_q = round(1/(wr_quarter/n_quarter))
    #and print the result
    print("You need the following number of wrappers:")
    print("Pennies: %d \nNickels: %d \nDimes: %d \nQuarters: %d" % (numwrap_c, numwrap_n, numwrap_d, numwrap_q))
    #validation


get_weights()
    
    
    
