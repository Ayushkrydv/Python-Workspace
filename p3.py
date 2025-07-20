num = int(input('enter your marks: '))
if(num>=90 and num<=100):
    print("ur grade is A")
elif(num>=80 and num<90):
    print('ur grade is B')
elif(num>=70 and num<80):
    print('ur grade is C')
elif(num>=60 and num<70):
    print('ur grade is D')
elif(num<60 and num>=0):
    print('ur grade is E')
else:
    print('invalid input')