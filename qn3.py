list = []
a = int(input("input number of element  in list:"))
for i in range(a):
    b = input("input element: ")
    list.append(b)
print(list)

for i in lst:
    for j in lst:
        if len(i) == len(j) and i != j:
            for b in range(len(i)):
                for b1 in range(len(j)):
                    if i[b] == j[b]:
                        res = j

    print("Anagram of {} is:".format(i), res)