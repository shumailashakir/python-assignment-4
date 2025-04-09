# Print 10 random numbers in the range 1 to 100.

import random

def main():

    random_numbers = [random.randint(1,100) for _ in range(10)]
    print(*random_numbers)


if __name__ == "__main__":   
    main() 