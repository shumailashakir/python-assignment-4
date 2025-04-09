# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

def main():
    fruits_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan" : 5.0,
        "mango": 7.0
    }

    total_cost = 0

    for fruit,price in fruits_prices.items():

       quantity = int(input(f"How many ({fruit}) do you want?:"))
       total_cost += quantity * price 

       print(f"\n Your total is $ {total_cost:.2f}")


if __name__ == "__main__":
    main()       