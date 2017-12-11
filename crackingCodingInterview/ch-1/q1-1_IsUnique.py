__author__ = 'pretymoon'


def isUnique(s):
    # without using any other data structure
    for i in range(len(s) - 1):
        j = i + 1
        for k in range(j + 1, len(s)):
            if s[i] == s[k]:
                return "Not Unique!"
    return "All Unique!"


def isUnique_set(s):
    # use a set!
    my_set = set()
    for i in range(len(s)):
        if s[i] in my_set:
            return "Not Unique!"
        else:
            my_set.add(s[i])
    return "All Unique"


print(isUnique("abca"))
print(isUnique_set("abcd"))