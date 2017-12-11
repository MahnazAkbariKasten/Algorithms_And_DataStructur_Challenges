__author__ = 'pretymoon'

def sumNum(s):
    n = 0
    tmp = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j].isdigit():
            tmp.append(s[j])
            j += 1
        if len(tmp) > 0:
            n += int("".join(tmp))
            tmp = []
        i = j + 1
    return n
print(sumNum("a123b111c"))
print(sumNum("1"))
print(sumNum("a"))
print(sumNum("zzz1aaa1bbb1ccc97ddd"))
print(sumNum("zzz000aaa000bbb000ccc000ddd"))