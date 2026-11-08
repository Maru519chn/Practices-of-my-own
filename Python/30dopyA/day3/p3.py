age = 96
height = 174
complexnum = 4j

pi = 3.14
e = 2.71
g = 9.81

base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

area_of_a_triangle = base * height / 2

print(f'The are of the triangle is: {area_of_a_triangle}')

side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))

perimeter = side_a + side_c + side_b

print(f'The perimeter of the triangle is {perimeter}')

rec_len = float(input('Enter the lenght of the rectangle: '))
rec_wid = float(input('Enter the width of the rectangle: '))

rec_perim = 2 * (rec_len + rec_wid)

print(f'The perimeter of the rectangle is {rec_perim}')

r = float(input('Enter the radius of the circle: '))

a_cir = pi * r ** 2
circ_cir = 2 * pi * r

print(f'The area of the circle is {a_cir} and its circumference is {circ_cir}')

m = int(input('Enter the slope of your line: '))
b = int(input('Enter the b value of your line: '))

slope = m
y_intercept = b
x_intercept = -b / m

print(f"Slope: {slope}")
print(f"y-intercept: (0, {y_intercept})")
print(f"x-intercept: ({x_intercept}, 0)")

print('Given the equation y = 2x - 2 and the points (2,2) and (6,10)')

axp = 2
ayp = 2
bxp = 6
byp = 10

# 1. Slope between the two points
slope_points = (byp - ayp) / (bxp - axp)

# 2. Euclidean distance between the two points
euclidean_distance = ((bxp - axp)**2 + (byp - ayp)**2)**0.5

# 3. Slope from Task 8 (y = 2x - 2)
slope_task8 = 2

print(f'Slope: {slope_points}')
print(f'Euclidean distance: {euclidean_distance}')

# 4. Compare the slopes
print('We compare their slopes!')
print(slope_points == slope_task8)

print('Now cuadratic functions!')
asq = int(input('Enter your a value: '))
bsq = int(input('Enter your b value: '))
csq = int(input('Enter your c value: '))

discriminant = bsq ** 2 - 4 * asq * csq

x1 = (-bsq + discriminant**0.5) / (2 * asq)
x2 = (-bsq - discriminant**0.5) / (2 * asq)

print(f'Solutions: x1 = {x1}, x2 = {x2}')

python = 'Python'
dragon = 'Dragon'
len(python) == len(dragon)
print(len(python) != len(dragon))  # Evaluates to False

print('on' in python.lower() and 'on' in dragon.lower())


course = 'I hope this course is not ful of JARGON'

print(len(float(str(python))))
print(len(float(str(dragon))))

print('jargon' in course.lower())

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

    