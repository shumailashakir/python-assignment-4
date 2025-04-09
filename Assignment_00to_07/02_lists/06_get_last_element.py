# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list.
# The list is guaranteed to be non-empty, but there are no guarantees on its length.


def get_first_element(lst):
    """ Prints the first element of a given non-empty list. """
    print("The Last element in the list is:", lst[-1])

def main():
    
    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  


    get_first_element(lst)


if __name__ == '__main__':
    main()