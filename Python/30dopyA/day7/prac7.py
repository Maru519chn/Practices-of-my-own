# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
tt = {'Twitter'}
ti_it_comp = it_companies.union(tt)

print(ti_it_comp)

more_it = {'Intel','NVIDIA','AMD','Samsung','Cisco','Dell','HP','Sony','Tencent','Alibaba','Adobe','Salesforce','Netflix','Spotify','Qualcomm','Broadcom','SAP','Accenture', 'Atlassian','Uber'}
# ngl I used AI to get all these IT companies bc I only knew NVIDIA bc of RAM prices

lot_of_it = ti_it_comp.union(more_it)
print(lot_of_it)

removed_item = lot_of_it.pop()

print(removed_item)

print(lot_of_it.difference(removed_item))

ab = A.union(B)
print(ab)


print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))

ba = B.union(A)

del ba
del ab
del A
del B

ages_set = set(age)

print('The difference bewteen strings, lists, tuples and sets are the following \nStrings: Contain alphanumeric characters or elements. \nList: Contain lists of elements between parenthesis; each one separated by a coma. \nTuples: Is a collection of different data types. \nSets: Is a collection of unordered and un-indexed items.')

sentence = "I am a teacher and I love to inspire and teach people."

clean_sentence = sentence.replace(".", "")

words = clean_sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))