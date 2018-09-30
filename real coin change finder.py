# change calculator

money = float(input('How much money did you pay?: $'))
cost = float(input('How much money did it cost?: $'))
money = money*100
cost = cost*100
quarter = 25
dime = 10
nickel = 5
penny = 1


money2 = money - cost
quarter2 = money2 // 25
money3 = money2 % 25
dime2 = money3 // 10
money4 = money3 % 10
nickel2 = money4 // 5
money5 = money4 % 5
penny2 = money5 // 1
money6 = money5 % 1

if quarter2 >= .5:
    print('Number of quarters: ', int(quarter2))
if dime2 >= .5:
    print('Number of dimes: ', int(dime2))
if nickel2 >= .5:
    print('Number of nickels: ', int(nickel2))
if penny2 >= .5:
    print('Number of pennies: ', int(penny2))
