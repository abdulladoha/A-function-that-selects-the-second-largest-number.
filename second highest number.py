def second_largest(numbers):
    if len(numbers) < 2:
        return None
    else:
        unique_numbers = list(set(numbers))
        unique_numbers.sort(reverse=True)
        return unique_numbers[1]

input = [1, 2, 3, 4]
print(second_largest(input))
