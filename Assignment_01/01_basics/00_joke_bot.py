# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:


PROMPT = "What do you want?"
JOKE = "Here is a joke for you! panaversity GPT - Sophia is heading out to the grocery store. A programer tells her: get a liter of milk .and if they have eggs get 12 .Sophia returns with 13 liters of milk . The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "I only tell jokes"


def main():

    user_input = input(PROMPT)

    if user_input == "Joke":
        print(JOKE)

    else:
        print(SORRY)   


if __name__  == "__main__":
    main()       

