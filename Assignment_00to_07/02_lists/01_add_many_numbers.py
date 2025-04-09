# Write a function that takes a list of numbers and returns the sum of those numbers.


def sum_Of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
        return total


def main():

    numbers_list = [10,20,30,40,50]  
    result = sum_Of_numbers(numbers_list) 

    print("List:", numbers_list)
    print("sum_of_numbers:",result)

if __name__ == "__main__":
    main()         



   