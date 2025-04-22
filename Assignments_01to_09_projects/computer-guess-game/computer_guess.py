import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low , high)

        feedback = input(f"Is guess too High (H), too Low (L), or correct (C)?").lower()


        if feedback == 'h':
            high = guess -1

        elif feedback == '1':
            low = guess +1

    print(f"The computer guess your number,{guess}, correctly!")


computer_guess(10)                