def filter_even_numbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

input_string = input("Enter a list of integers separated by spaces: ")
input_list = list(map(int, input_string.split()))

result = filter_even_numbers(input_list)
print(f"The even numbers from the list are: {result}")
