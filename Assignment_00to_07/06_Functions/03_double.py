# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.


def double(num):
    return num * 2

def main():
    num = int(input("\033[94mEnter a number \033[0m"))
    result = double(num)
    print(f"Double that's is {result}")

if __name__ == "__main__":   
    main() 

