num = int(input('Enter a num: '))
if(num%5==0):
    if(num%10==0):
        print('0')
    else:
        print('5')
else:
    print('other')
