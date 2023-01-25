
lower = eval(input(" enter a lower bound: "))

even_list = []
odd_list = []

while lower < 0:   
    lower = eval(input("Please enter a positive number: "))
else:
    upper = eval(input(" enter a upper bound: "))
    
    for a in range(lower,upper+1):
        if a %2 == 0:
            even_list.append(a)
        else:
            odd_list.append(a)

print(" even numbers are: ", even_list)
print(" odd numbers are: ", odd_list)