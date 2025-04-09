#  In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.


def add_three_copies(my_list, data):
    """ Adds three copy of data to the given list  (mutable behavior) """


    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():

    message = input("Enter a message to copy:") 

    my_list = []  
    print("List before:" , my_list) 

    add_three_copies(my_list , message)
    print("List_after:", my_list)


if __name__ == "__main__" :
    main()   