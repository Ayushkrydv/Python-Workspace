print('travel from city A to City B')
time = int(input('enter time'))
longer = int(input('what u mean by longer'))
if(time<=longer):
    price = int(input('enter price'))
    higher = int(input("define higher"))
    if(price<higher):
        print("red eye flight")
        
    else:
        print('Daytime flight')
else:
    price = int(input('enter price'))
    higher = int(input("define higher"))
    if(price>higher):
        print('Train')
    else:
        print('coach')
print('arrive city b')