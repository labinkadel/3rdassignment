a = input("Enter a string:")
print(f'Given String: {a}')
revstr = a[::-1]
print(f'Reversed String: {revstr}')


def is_palindrome(a, revstring):
    if revstring == a:
        return f"The input word is same if reversed"
    else:
        return f"Not same"


print(is_palindrome(a, revstr))