__author__ = 'pretymoon'
"""
ACCEPTED
"""
def are_isomorphics(s, t):
    if len(s) != len(t):
        return False
    dict = {}
    for i in range(len(s)):
        if s[i] in dict:
            if dict[s[i]] != t[i]:
                return False
        else:
            if t[i] in dict.values():
                return False
            else:
                dict[s[i]] = t[i]
    return True

print(are_isomorphics("ab", "aa"))
print(are_isomorphics("aa", "ab"))
# print(are_isomorphics("fee", "loo"))
# print(are_isomorphics("feee", "loo"))
# print(are_isomorphics("falfe", "palse"))
