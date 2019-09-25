def multiplication_table():
    maxval= int(input("Choose your highest number: "))
    maxlength = len(str(maxval*3))
    print(type(maxval))
    for i in range(1, maxval + 1):
        for j in range(1, maxval + 1):
                print (str(j*i).rjust(maxlength,' '))
        print

multiplication_table()
