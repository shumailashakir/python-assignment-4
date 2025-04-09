# Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!). Thus, your program should produce the following sample run:

def main():
    MAX_VALUE = 10000

    a, b = 0, 1

    while a < MAX_VALUE:   
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__": 
    main()  


