weight = float(input('weight: '))
unit = input("(L)bs OR (K)g: ")

if unit.upper() == "L":
    convert = weight * 0.45
    print(f'you are {convert} kilos')
else:
    convert = weight/0.45
    print(f"you are {convert} pounds")