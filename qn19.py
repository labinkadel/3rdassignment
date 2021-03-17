class PythonValidate:
    @staticmethod
    def val_paren(s):
        list, dic = [], {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in dic:
                list.append(i)
            elif len(list) == 0 or dic[list.pop()] != i:
                return False
        return len(list) == 0


print(PythonValidate().val_paren("(){}[]"))
print(PythonValidate().val_paren("()[{)}"))

