# to count the number of positive numbers in a list of numbers.

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]

def count_positive_numbers(numbers):
    return len([num for num in numbers if num > 0])

print(count_positive_numbers(numbers))