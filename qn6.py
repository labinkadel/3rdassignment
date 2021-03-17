list = []
A = int(input("Enter the number of friends: "))
for i in range(A):
    k = input("Enter name: ")
    list.append(k)
print(list)
if 'John' in list:
    print("Found")
else:
    print("Not Found")
