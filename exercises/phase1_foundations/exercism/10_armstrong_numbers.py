def is_armstrong_number(number):
    list_number = [int(digit) for digit in str(number)]
    powered_numbers = [digit ** len(list_number) for digit in list_number]

    return sum(powered_numbers) == number
