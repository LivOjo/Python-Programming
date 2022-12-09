#welcome statement
print('Welcome to Tip calculator!')
#Input for total bill
bill=int(input('what is your total bill? $'))
print()
#Input for percentage tip, 2, 3, 5
percent_tip=float(input('what is your tip? 5%,10%,15% '))
print()
#input for number of people to
people=int(input('how may people are sharing the bill? '))
print()
#tip calculation;
tip=(percent_tip/100)*bill
print()
#bill plus tip : total bill + tip#
total_bill=(bill)+tip
print()
#bill per person: bill plus tip/ number of people
bill_per_p=(total_bill)/people
print()
#round up bill per person to 2 decimal place using round() function
rounding=round(bill_per_p,2)
print()
#print out " Each person should pay $_____ "
print(f'Each person should pay $ {rounding}')
print()
print()
print('Thank you for using tip calculator!')