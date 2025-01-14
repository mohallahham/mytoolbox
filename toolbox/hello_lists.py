import random

numbers = []

#generate 10 random numbers from 1-100 and add them to the list 
for i in range(1,10):
    numbers.append(random.randint(1,100))
print(f'Our list for the day is:\n{numbers}')
print(f'The smallest number is {min(numbers)} and the largest is {max(numbers)}')
print(f'did you know these numbers add up to {sum(numbers)}')

