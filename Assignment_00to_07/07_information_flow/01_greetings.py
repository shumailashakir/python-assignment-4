# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.
#  Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

def greet(name):
    """Print a greeting with the given name """
    print(f"greetings {name}!:")


def main():
    name = input("What's your name?")

    greet(name)  


if __name__ == "__main__":
    main()      

def greet(name):
    """Prints a greeting with the given name."""
    print(f"Greetings {name}!")

def main():
    # Ask the user for their name
    name = input("What's your name? ")
    
    # Call the greet function with the user's name
    greet(name)

# Required line to run the program
if __name__ == '__main__':
    main()    