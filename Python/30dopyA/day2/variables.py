# Day 2: 30 Days of python programming

first_name = 'Maru'
last_name = 'Chacón'
full_name = 'Maru Chacón'
Country = 'Costa Rica'
City = 'Puntarenas'
Age = 96
Year = 2026
is_married = False
is_true = False
is_light_on = True
weightinlb, heightinft, weightinkg, heightincm = 214, "5'7", 97, 174

print(type(first_name))  # str
print(type(last_name))  # str
print(type(full_name))  # str
print(type(Country))  # str
print(type(City))  # str
print(type(Age))  # int
print(type(Year))  # int
print(type(is_married))  # bool
print(type(is_true))  # bool
print(type(is_light_on))  # bool
print(type(weightinlb))  # int
print(type(heightinft))  # str
print(type(weightinkg))  # int
print(type(heightincm))  # int

first_message_length = len(first_name)
first_and_last_length_comparison = len(first_name) == len(last_name)
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
floor_division = num_one // num_two
exponential = num_one ** num_two

area_of_circle = 3.14 * (30 ** 2)
circum_of_circle = 2 * 3.14 * 30
radius_of_circle = input("Enter radius of a circle: ")
area_of_circle = 3.14 * (int(radius_of_circle) ** 2)
circum_of_circle = 2 * 3.14 * int(radius_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")