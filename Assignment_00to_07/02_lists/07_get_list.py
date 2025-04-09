# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses
#  enter without typing anything, print the list.


def main():

    lst = []

    while True:
        value = input("Enter a value:")
        if value == "" :
            break


            lst.append(value)

            print("Here's the List:" ,lst)


if __name__ == "__main__" :
    main()            