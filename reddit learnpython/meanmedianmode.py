import collections

def get_mean(n,e):
    totalsum = sum(n)
    totalitems = float(len(n))
    mean = (totalsum/totalitems)
    roundedmean = round(mean,e)
    print("Mean: " + str(roundedmean))

def get_median(n):
    #find the length of the list
    nlen = len(n)
    #sorting list from low to high
    n.sort()
    if nlen % 2 == 0:
        median1 = n[int(nlen/2)]
        median2 = n[int(nlen/2 -1)]
        median = (median1 + median2)/2
    else:
        median = n[int(nlen/2)]
    print("Median: " + str(median))

def get_mode(n):
    #calculate frequency
    data = collections.Counter(n)
    data_list = dict(data)
    #find highest frequency
    max_freq = max(list(data.values()))
    mode_val = [num for num,freq in data_list.items() if freq == max_freq]
    if len(mode_val) == len(n):
        print("No mode in this list.")
    else:
        print("Modes: " + ", ".join(map(str,mode_val)))
    

def questions():
    numbers = [1,2,3,4,5,6,7,8.25252525252525,9,10,10,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    print("Are you using the pre-built number list?")
    yesno = input().lower()
    if yesno == "no":
        num = input("Please type the numbers you want to consider in a space separated list.").split()
        numbers = [float(i) for i in num]
    print("How many decimals place do you want to report the mean?")
    decimals = int(input())
    get_mean(numbers,decimals)
    get_median(numbers)
    get_mode(numbers)
  

    

        

    
        
    
