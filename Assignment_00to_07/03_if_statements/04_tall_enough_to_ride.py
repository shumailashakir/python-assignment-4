# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.


def main():
    while True:

        height = input("How tall are you?")

        if height == "" :

            print("Exiting the program.Have a great day!")
            break

        height = int(height)  

        if height >= 50:
            print( "You're tall enough the ride!\n")  
        else:
            print("You're not tall enough the ride. but maybe next year! \n")  


if __name__ == "__main__":   
    main()           