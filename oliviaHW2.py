#1
twenty=[]
for values in range(1,21):
    print(values)
print()
#2
for values in range(1,101):
    print(values)
print()
#3
hundred_two=list(range(1,101))
print(f'the minimum value in the list hundred_two is {min(hundred_two)}')
print(f'the maximum value in the list hundred_two is {max(hundred_two)}')
print(f'the sum of all the items in the list hundred_two is {sum(hundred_two)}')
print()
#4
for values in range (1,21,2):
    print(values)
print()
#5
threes=[values *3 for values in range (1,31)]
print(threes)
print()
#6
for values in range(1, 11):
    print(values**3)
print()
#7
list=[values**3 for values in range(1, 11)]
print(list)

