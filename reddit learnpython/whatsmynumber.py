#challenge criteria:
#number is >= 10 +
#number is prime +
#number does not have a 1 or a 7  +
#sum of all digits <= 10 +
#first two digits sum to odd +
#second to last digit is even +
#last digit is equal to how many digits in the number -

def find_number():
    guess_list = []
    notPrime = [1]
    
    #number is >= 10
    for i in range(1,1001):
        if i >= 10:
            guess_list.append(i)
            
    #populate list of not Prime numbers
    for num in guess_list:
        for i in range(2,num+1):
            if int(num) % int(i) == 0 and num != i and notPrime[-1] != num:
                notPrime.append(num)


    #any type of manipulation on the digits themselves is done here
    for num in guess_list:
        digits = [int(d) for d in str(num)]
        #remove all digits with a 1 or 7
        if 1 in digits or 7 in digits:
            notPrime.append(num)
        #remove all digits whose sum > 10
        if sum(digits) > 10:
            notPrime.append(num)
        #remove all digits whose sum is even
        if (digits[0] + digits[1]) % 2 == 0:
            notPrime.append(num)
        #remove all digits in which the second to last place are odd (including 0)
        if digits[-2] % 2 != 0 or digits[-2] == 0:
            notPrime.append(num)
        #remove all digits where the last number is not the length of the digit
        if digits[-1] != len(digits):
            notPrime.append(num)
    
    #this parses our list of rejected attempts and removes them from the guess list        
    for digit in notPrime:
        if digit in guess_list:
            guess_list.remove(digit)

    print(guess_list[0])

    


find_number()
            
