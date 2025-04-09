# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.


def main():

    num_counts = {}

    while True:

        user_input = input("\033[94m Enter a number(or press Enter to stop):\033[0m")

        if user_input == "":
            break

        number = int(user_input)


        if number in num_counts:
            num_counts[number] += 1
        else:
            num_counts[number] = 1


            print("\n Number occurrences:")

            for num, count in num_counts.items():
                print(f"{num} appears {count} times.")


if __name__ == "__main__":
    main()
