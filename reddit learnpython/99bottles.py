def bottles():
    while True:
        n = ''
        try:
            n = int(input("How many bottles do you want to start with? "))
        except ValueError:
            print ("Please enter a whole number.")
        if type(n) == int:
            break
    while n > 0:
        new_n = n - 1
        n_bot = "bottles"
        newn_bot = "bottles"
        if n == 1:
            n_bot = "bottle"
        if new_n == 1:
            newn_bot = "bottle"
        print ("%d %s of beer on the wall, %d %s of beer. Take one down, pass it around, %d %s of beer on the wall." % (n,n_bot,n, n_bot,new_n,newn_bot))
        print ('')
        n = new_n
            
