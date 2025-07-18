name = input("Enter name: ")
length = len(name)
if length < 3:
    print("name must be at least 3 char")
elif length > 50:
    print('name can be max of 50 char')
else:
    print('name looks good')