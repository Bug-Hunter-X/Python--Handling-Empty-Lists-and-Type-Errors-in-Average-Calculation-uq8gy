def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    my_list = []
    result = calculate_average(my_list)
    print(f"The average is: {result}")  # Output: 0

    my_list = [10, 20, 30, 40, 50]
    result = calculate_average(my_list)
    print(f"The average is: {result}")  # Output: 30.0

    my_list = [10, 20, 'a']
    result = calculate_average(my_list) # Raises ValueError
    print(f"The average is: {result}")
except ValueError as e:
    print(f"Error: {e}") # Output: Error: List must contain only numbers.