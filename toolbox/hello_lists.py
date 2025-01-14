import random

numbers = []
# odd_numbers =[]
# even_numbers =[]
grades = []

#generate 10 random numbers from 1-100 and add them to the list 
for i in range(1,10):
    numbers.append(random.randint(1,100))
print(f'Our list for the day is:\n{numbers}')
print(f'The smallest number is {min(numbers)} and the largest is {max(numbers)}')
print(f'did you know these numbers add up to {sum(numbers)}\n')

split_list = input('Do you want to split to odd and even numbers? ').lower()

if split_list == 'yes':
# detecting odd and even numbers!
    # for number in numbers:
    #     if number % 2 == 0:
    #         even_numbers.append(number)
    #     else:
    #         odd_numbers.append(number)
    even_numbers = [x for x in numbers if x % 2 == 0] #list comprehension
    odd_numbers = [x for x in numbers if x % 2 != 0]
    print(f'This is a list of even numbers:\n {even_numbers}\n and this is a list of odd numbers: \n {odd_numbers}')

grading = input('Do you want to covert the list to A-F grading scale? ').lower()

if grading == 'yes':
        
    #Grading system
    for number in numbers:
        if number >= 90:
            grades.append('A')
        elif number < 90 and number >= 80:
            grades.append('B')
        elif number < 80 and number >= 70:
            grades.append('C')
        elif number < 70 and number >= 60:
            grades.append('D') 
        else:
            grades.append('F')

    print(f'This is our list in a grading system \n {grades}')

    grade_summary = input('Do you want a summary of all grades? ').lower()

    if grade_summary == "yes":
    #printing using the zip function
        for number, grade in zip(numbers, grades):
            print(f'you have scored {number}, and your grade is {grade}')




