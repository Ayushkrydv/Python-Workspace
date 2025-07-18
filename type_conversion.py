birth_year = input('birth year: ')
# [age = 2025-birth_year]
# here error is birth year variable is storing string not number. so we have to use type conversion
age = 2025 - int(birth_year)
print(type(birth_year))
print(type(age))
print(age)