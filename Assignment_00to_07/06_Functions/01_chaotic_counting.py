# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. 


import random

DONE_LIKELIHOOD = 0.2

def done():

    """Return True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD


def chaotic_counting():
    """Counts from 1 to 10 but stops early if done() return True """    
    for i in range(1,11):
        if done():
            return
        print(i, end= " ")

def main():
    print("I am going to count until 10 or until I feel like stopping,whichever come first. ")
    chaotic_counting
    print("\nI am done.")  

if __name__ == "__main__":
    main()          
