'''
1. welcome statement
2. print out arithmetic operators available(addition, subtraction, multiplication, division, exponential)
3. 2 user input for integers
4. performing operations based on users choice and input
5. lastly print out answers
'''

print('Welcome to the simple calculator  ')
print()
print('''
    0: Addition 
    1: Subtraction
    2: Multiplication
    3: Division
    4: Exponential
''')

operator=input('Choose a number corresponding to the arithmetic operator you wish to use above: ')
num_1=int(input('enter the first number: '))
num_2=int(input('enter the second number: '))
print()
if operator =='0':
   answer= num_1 + num_2
   print(f'{num_1} + {num_2} = {answer}')

elif operator =='1':
   answer= num_1 - num_2
   print(f'{num_1} - {num_2} = {answer}')

elif operator =='2':
   answer= num_1 * num_2
   print(f'{num_1} * {num_2} = {answer}')

elif operator =='3':
   answer= round(num_1 / num_2, 3)
   print(f'{num_1} / {num_2} = {answer}')

elif operator == '4':
   answer = num_1 ** num_2
   print(f'{num_1} ^ {num_2} = {answer}')
