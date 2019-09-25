def find_nth():
    getting_input = True
    while getting_input:
        n = ''
        try:
            n = int(input("Fibonnaci Term Desired: "))
        except ValueError:
            print("Please insert an integer.")
        if type(n) == int:
            getting_input = False
    print("The %d term of the Fibonacci Sequence is %s" % (n,str(fibonacci(n))))

def fibonacci(n):
    fib_list = []
    for i in range(n):
        if i == 0:
            fib_list.append(i)
        elif i == 1:
            fib_list.append(i)
        else:
            fib_sum = fib_list[-1] + fib_list[-2]
            fib_list.append(fib_sum)
    return fib_list[-1]
        
    
        
find_nth()
        
