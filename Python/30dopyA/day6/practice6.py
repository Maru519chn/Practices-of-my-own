empty_tuple = ()

brothers = ('Frankling', 'Ferdinand', 'Fercho')
sisters = ('Francini', 'Fernanda', 'Felicia')
siblings = brothers + sisters

print(len(siblings))

parents = ('Francis', 'Fiona')

family_members = siblings + parents

print(family_members)

#unpack stuff

*unpacked_siblings, father, mother = family_members
print('Siblings:', unpacked_siblings)
print('Parents:', father, mother)

fruits = ('Apple', 'Pineapple', 'Banana', 'Tomato')
veggies = ('Onion', 'Garlic', 'Cucumber', 'Carrot')
# Is ginger a veggie?????
meat = ('T-bone', 'Chicken Nuggets', 'Lamb Ribs', 'Pork Chops')

food_stuff_tp = fruits + veggies + meat

print(food_stuff_tp)

food_stuff_list = list(food_stuff_tp)

mid = len(food_stuff_list) // 2

middle_item = food_stuff_list[mid]
print ('Middle item:', middle_item)

first_three = food_stuff_list[:3]
last_three = food_stuff_list[-3:]

print('First three:', first_three)
print('Last three:', last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)