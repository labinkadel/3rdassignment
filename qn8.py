a = int(input("Enter a number: "))

def is_prime(a):
    if a < 2:
        return False
    if a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0 and a != i:
                return False
    return True


print(is_prime(a))
