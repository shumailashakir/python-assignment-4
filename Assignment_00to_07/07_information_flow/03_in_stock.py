# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "mango": 250,
        "orange": 700
    }

    return inventory.get(fruit.lower(),0)


def main():
    fruit = input("Enter a fruit:").strip()


    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is stock.Here is how many:")
        print(stock)

    else:
        print("This fruit is not in stock.")


if __name__ == "__main__":
    main()            

     




  



