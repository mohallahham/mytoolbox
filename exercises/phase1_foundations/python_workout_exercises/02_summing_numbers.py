# Function to calculate the sum of an arbitrary number of arguments
def mysum(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


print(mysum(1, 2, 3))  # Output: 6


# Function to calculate the sum of a list of numbers with an optional starting value
def mysum(numbers, start=0):
    total = start
    for number in numbers:
        total = total + number
    return total


print(mysum([1, 2, 3], 6))  # Output: 12


# Function to calculate the average of a list of numbers with zero-division handling
def myavg(numbers):
    numbers_count = len(numbers)
    if numbers_count == 0:
        print("You can't divide by zero")
        return None
    avg = mysum(numbers) / numbers_count
    return avg


print(myavg([]))  # You can't divide by zero
print(myavg([10, 20]))  # Output: 15.0
