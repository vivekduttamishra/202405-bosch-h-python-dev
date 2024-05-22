def sum(*numbers):
    result =0
    for number in numbers:
        result += number


def average(*numbers):
    return sum(*numbers)/len(numbers)
