for num in range (1,101):
    if num % 2==0 and num % 6==0:
        print('Buzz')
    elif num % 6 == 0:
        print('Fizz')

    elif num % 2 == 0:
     print('FizzBuzz')

    else:
        print(num)
