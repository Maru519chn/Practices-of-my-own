print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

words = ['Coding', 'For', 'All']
print(' '.join(words))

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

first_word = company[0:6]
print(first_word)
print(company.find('Coding'))
print(company.index('Coding'))
print('Coding' in company)

print(company.replace('Coding', 'Python'))

phrase = 'Python For Everyone' 
print(phrase.replace('Everyone', 'All'))

print(company.split(' '))

# Is there a way where I do not get those ugly "[]" symbols?

tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(", "))

print(company[0])

last_index = len(company) -1
print(last_index)

print(company[10])

acronym = "".join([word[0].upper() for word in phrase.split()])
print(acronym)
acronym_for_code = "".join([word[0].upper() for word in company.split()])
print(acronym_for_code)

print(company.index('C'))
print(company.index('F'))

phrase_1 = 'Coding For All People'
print(phrase_1.rfind('l'))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))

print(sentence.rindex('because'))

start = sentence.find('because')
end = sentence.rindex('because') + len('because')
sliced_phrase = sentence[start:end]
print(sliced_phrase)


print(sentence.find('because'))

print('Coding For All'.startswith('Coding'))

padded_str = '  Coding For All  '
print(padded_str.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier()) # I had forgot a period before the "isidentifier"

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libs))

sentences = 'I am enjoying this challenge.\nI just wonder what is next.'

table = 'Name\tAge\tCountry\tAsabeneh\t250\tFinland\tHelsinki'
print(table)

radius = 10
area = 3.14 * radius ** 2
print(
    f'The area of a circle with radius {radius} is {int(area)} meters square'
)

#FINALLY LAST ONE

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")