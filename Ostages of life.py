#StagesOfLife
old=int(input('state a person\'s age:\n'))#telling person to input a number of age
if old <2:#if persons age is less than 2 print That person is a really young (baby)
    print('That person is a really young (baby)')
elif old <5:#if persons age is less than 5 print That person is a toddler
    print('That person is a toddler')
elif old <10:#if persons age is less than 10 print That person is a kid
    print('That person is a kid')
elif old <12:#if persons age is less than 12 print That person is a tween
    print ('That person is a tween')
elif old <20:#if persons age is less than 20 print That person is a teenager
    print('That person is a teenager')
elif old <55:#if persons age is less than 55 print That person is an adult
    print('That person is an adult')
else:#else that person is old
    print('That person is old')