list = []
print(id(list))
list = []
n = int(input("Enter number of elements in list: "))
for i in range(n):
    a = input("Enter the element: ")
    list.append(a)
print(list)
print(id(list))
sorted_list = sorted(list)
print(sorted_list)
print(f'The first item on list: {sorted_list[0]}')
print(f'The second item on list: {sorted_list[1]}')