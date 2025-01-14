#First line of code
print('Hello, World')

#lists 
facts = ['''A shrimp's heart is in its head.''', '''"Dreamt" is the only English word that ends in the letters "mt".''' ]

#simple string manipulation
name = input(f'Welcome to my toolbox, what is your name? \n')
print(f'Hello, {name.title()} a pleasure to meet you\nHere is your name in different styles:\n\t Lower Case: {name.lower()}\n\t Upper Case: {name.upper()}\n\t Title: {name.title()}\n Did you know that:\n 1- {facts[0]}\n 2- {facts[1]}\n' )

#asks user to remove a fact
index= int(input(f' please select 1 or 2 to remove a fact from our list\n'))

#used pop instead of remove to use the value again here
popped_fact = facts.pop(index-1)
print(f'you have removed {popped_fact} from our list\n')


#asks user to add a fact
new_fact = input(f' Please add a replacement fact to our list\n')

#this adds a fact to the end of the list
facts.append(new_fact)
print(f'thank you for letting me know that: \n\t {facts[-1]}.')
print(f' Our new facts are: \n\t 1-{facts[0]}\n\t 2-{facts[1]}.')






