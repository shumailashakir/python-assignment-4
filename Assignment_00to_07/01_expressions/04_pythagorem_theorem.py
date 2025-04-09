# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!


import math  

def main():
    ab = float(input("\033[1m\033[3mEnter the length of AB:\033[0m "))  
    ac = float(input("\033[1m\033[3mEnter the length of AC:\033[0m "))  

    bc = math.sqrt(ab**2 + ac**2)  

    print(f"The length of BC (the hypotenuse) is: {bc}")  

if __name__ == '__main__':
    main()