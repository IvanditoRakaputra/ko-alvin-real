
def addition(x,y):
    return x + Y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def power(x,y):
    return x**y

def division(x,y):
    return x/y

print("Select the operation below: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Power")
print("5. Division")

while True:
    number = input(' Enter the numbers from the list above(1/2/3/4/5): ')

    if number in ('1' , '2' , '3' , '4' , '5'):
        number_1 = eval(input("Enter the first number: "))
        number_2 = eval(input("Enter the second number: "))

        if number == '1':
            print(number_1, "+", number_2, "=", addition(number_1, number_2))

        elif number == '2':
            print(number_1, "-", number_2, "=", substraction(number_1, number_2))

        elif number== '3':
            print(number_1, "*", number_2, "=", multiplication(number_1, number_2))

        elif number== '4':
            print(number_1, "**", number_2, "=", power(number_1, number_2))

        elif number == '5':
            print(number_1, "/", number_2, "=", division(number_1, number_2))

        Next = input("next? (yes/no): ")
        if Next == "no":
          break
    
    else:
        print("Enter A Valid Number From 1-5")