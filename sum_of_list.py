def sum_of_list():
    number_of_elements = int(input("How many numbers do you want to add to the list?"))
    numbers=[]

    for i in range(number_of_elements):
        number = float(input(f"Enter your number{i+1}:"))
        numbers.append(number)
    
    total = sum(numbers)
    return total
result = sum_of_list()
print(f"The sum of the numbers in the list is: {result}")