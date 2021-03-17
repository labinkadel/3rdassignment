friends = []
frn1 = ('labin', 'kadel', 25)
frn2 = ('sandis', 'prajapati', 21)
friends.append(frn1)
friends.append(frn2)
print(friends)
age = []
for i in range(len(friends)):
    age.append(friends[i][2])
print(age)
avg = sum(age)/len(age)
print(f'The average age is: {avg}')
for i in range(len(friends)):
    if friends[i][2] > avg:
        print(f'{friends[i][0]} is old')
    else:
        print(f'{friends[i][0]} is young')