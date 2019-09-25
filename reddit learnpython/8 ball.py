import time
import random
import sys

replies = ["Yes", "No", "Not sure", "Ask a friend", "You might die!"]

def ask():
    print ("What is your question?")
    quest = input()
    print ("Thinking...")
    time.sleep(3)
    print (replies[random.randint(0,4)])
    end()

def end():
    ans = input("Do you want to play again? ").lower()
    if ans == "yes":
        ask()
    else:
        print ("Thanks for playing!")
        sys.exit()

ask()
        
    
