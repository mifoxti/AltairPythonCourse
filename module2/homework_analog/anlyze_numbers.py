def analyze_numbers(numbers):
    if not numbers:
        return {
            "sum": 0,
            "average": 0,
            "min": None,
            "max": None,
            "even_numbers": [],
        }

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return {
        "sum": total_sum,
        "average": average,
        "min": min_number,
        "max": max_number,
        "even_numbers": even_numbers
    }


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [15, 22, 8, 3, 17]

empty_list = []

print(analyze_numbers(numbers1))
print(analyze_numbers(numbers2))
print(analyze_numbers(empty_list))