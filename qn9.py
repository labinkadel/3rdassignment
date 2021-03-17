list = []
a = int(input("Enter num of elements in list: "))
for i in range(a):
    k = int(input("Enter element to add: "))
    list.append(k)
print(list)
f = int(input("Enter element to find: "))


def binary_search(list, f):
    for i in range(len(list)):
        if f in list:
            return f'The index of {f} is: {list.index(f)}'
        else:
            return -1


print(binary_search(list, f))