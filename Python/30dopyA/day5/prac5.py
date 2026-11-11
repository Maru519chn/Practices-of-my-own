# Declare an empty list

empty_list = list()
list_with_5 = ['Caldosa', 'Granizado', 'Ceviche', 'Churchill', 'Apretados']
print(len(list_with_5))

print(list_with_5[0])
print(list_with_5[2])
print(list_with_5[4])

mixed_data_types = ['Maru', '18yo', '174cm', 'unmarried', 'Puntarenas, Costa Rica']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)
print('The IT companies list has:', len(it_companies), 'companies.')

print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

it_companies.insert(4, 'NVIDIA')
it_companies[0] = it_companies[0].upper()

joined_companies = '#; '.join(it_companies)
print(joined_companies)

print('IBM' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

companies_sliced = it_companies[0:3]
print(companies_sliced)

companies_sliced_end = it_companies[3:6]
print(companies_sliced_end)

mid_index = len(it_companies) // 2
middle = it_companies[mid_index : mid_index + 1]
print(middle)

print(it_companies.pop(0))
print(it_companies.pop(4))
print(it_companies.pop(5))

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = back_end + front_end + ['Python', 'SQL']
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f'Sorted ages: {ages}')
print(f'Min age: {min_age}, Max age: {max_age}')

ages.append(min_age)
ages.append(max_age)
ages.sort()
print(f'List after adding min and max: {ages}')

median_age = (ages[5] + ages[6]) / 2
print('Median:', median_age)

average_age = sum(ages) / len(ages)
print('Average:', average_age)

age_range = max_age - min_age
print('Range:', age_range)

diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
print("abs(min - avg):", diff_min)
print("abs(max - avg):", diff_max)
print("Are they equal?:", diff_min == diff_max)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

mid_index = len(countries) // 2
middle_country = countries[mid_index]

print('Country in the middle', middle_country)

first_half = countries[:4]
second_half = countries[4:]
print('First half:', first_half)
print('Second half:', second_half)

c1, c2, c3, *scandic_countries = countries
print("Primeros tres:", c1, c2, c3)
print("Scandic countries:", scandic_countries)

# Today was something more easier
# I hope I still this motivated tomorrow