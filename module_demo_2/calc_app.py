import utils.console as console


def main():
    while True:
        print('Welcome to Calculator')

        choice = read_int("1. plus 2. minus, 3. multiply 4. divide 0. exit?")
        
        if choice == 0:
            break
        
        num1 = console.read_int("Enter first number")
        num2 = console.read_int("Enter second number")


        if choice == 1:
            print(num1 + num2)
        elif choice == 2:
            print(num1 - num2)
        elif choice == 3:
            print(num1 * num2)
        elif choice == 4:
            print(num1 / num2)
        else:
            print("Invalid choice")


main()