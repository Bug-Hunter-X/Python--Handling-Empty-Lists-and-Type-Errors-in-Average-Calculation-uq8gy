def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") # This will return 0

my_list = [10,20,30,40,50]
result = calculate_average(my_list)
print(f"The average is: {result}") # This will return 30.0

my_list = [10, 20, 'a']
result = calculate_average(my_list) # TypeError: unsupported operand type(s) for +: 'int' and 'str'