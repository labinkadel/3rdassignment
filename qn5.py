tupA = ('labin', 'kadel', 27)
people = []
people.append(tupA)
print(people)
tupB = ('Aman', 'Kc', 25)
tupC = ('Bicky', 'Bc', 21)
people.append(tupB)
people.append(tupC)
# before sorting
print(f'Before sorting by age: {people}')
# sorting with age
people.sort(key=lambda x: x[2])
# after sorting with age
print(f'After sorting by age: {people}')
