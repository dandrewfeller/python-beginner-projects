def get_triples():
    #need a function to get the input and convert to integer
    print("Please enter the length of all three sides of the triangle with a space separating each.")
    x,y,z = input().split()
    a = int(x)
    b = int(y)
    c = int(z)
    triple_sorter(a,b,c)

def triple_sorter(d,e,f):
    #passing that function into here, then sorting triples
    a = d
    b = e
    c = f
    if d > e and d > f:
        a = e
        b = f
        c = d
    elif e > d and e > f:
        a = d
        b = f
        c = e
    pyth_check(a,b,c)

def pyth_check(a,b,c):
    pytag = a*a + b*b
    if pytag != c*c:
        print("Sorry, your triangle with lengths %d %d %d is NOT a pythagorean triangle." % (a,b,c))
    else:
        print("The triangle with lengths %d %d %d is a pythagorean triangle." % (a,b,c))

get_triples()
        


