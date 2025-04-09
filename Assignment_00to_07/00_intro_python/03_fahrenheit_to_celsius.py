# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the 
# temperature converted to Celsius.




def main():

    fahrenheit = float(input(" \033[1;3m Enter tempreature in fahrenheit: \033[0m"))

    celsius =  (fahrenheit - 32) * 5.0/9.0

    print(f"tempreature : {fahrenheit} F = {celsius} C")

if __name__ == '__main__':
    main()    

