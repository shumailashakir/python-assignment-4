

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.0

def count_even():
    lst = []

    while True:
        user_input = input("Enter an integer or press enter to stop:")

        if user_input =="":
            break
        try:
            num = int(user_input)   
            lst.append(num) 
        except ValueError:
            print("Invalid input.Please enter an integer.")

        even_count = sum(1 for num in lst if sum % 2 == 0 )

        print(f"Numbers of even numbers: {even_count}")

def main():
    count_even()   


if __name__ == "__main":
    main()   


 












  









                                                                                                                                         













