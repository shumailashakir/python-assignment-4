# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5



def main():

    side1 = float(input(" \033[1;3m Enter the length of side 1: \033[0m "))
    side2 = float(input(" \033[1;3m Enter the length of side 2: \033[0m"))
    side3 = float(input(" \033[1;3m Enter the length of side 3: \033[0m"))

    perimeter = side1 + side2 + side3

    print(f"The perimeter of the triangle is {perimeter}")


if __name__ == "__main__":
    main()    