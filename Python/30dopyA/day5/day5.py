# 5th day. I'm tired of this. I've been carrying calc within this.
# Gotta stay positive twin

#LISTS

# Empty lists
ist = list()
ist = []

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']


print('Fruits: ', fruits)
# Don't forget the coma

# pop deletes an itmem. With argument '' it deletes the last item.

del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined

# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
