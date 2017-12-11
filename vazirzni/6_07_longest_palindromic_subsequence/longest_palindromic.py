__author__ = 'pretymoon'

# myString = "ACGTGTCAAAATCG"
# myString="ABAAABA"
myString="AAB"

table = {}
pal = {}

def lps(s, e):
    if (s, e) in table:
        return table[(s, e)]
    elif e == s:
        table[(s, e)] = 1
        pal[(s, e)] = myString[s]
        return table[(s, e)]
    elif e == s + 1:
        if myString[s] == myString[e]:
            table[(s, e)] = 2
            pal[(s, e)] = myString[s:e+1]
            return table[(s, e)]
        else:
            table[(s, e)] = 1
            pal[(s, e)] = myString[s]
            return table[(s, e)]
    elif myString[s] == myString[e]:
        if (s+1, e-1) not in table:
            table[(s+1, e-1)] = lps(s+1, e-1)
        table[(s, e)] = 2 + table[(s+1, e-1)]
        pal[(s, e)] = myString[s] + pal[(s+1, e-1)] + myString[e]
        return table[(s, e)]
    else:
        if (s+1, e) not in table:
            table[(s+1, e)] = lps(s+1, e)

        if (s, e-1) not in table:
            table[(s, e-1)] = lps(s, e-1)

        if table[(s+1, e)] > table[(s, e-1)]:
            table[(s, e)] = table[(s+1, e)]
            pal[(s, e)] = pal[(s+1, e)]
        else:
            table[(s, e)] = table[(s, e-1)]
            pal[(s, e)] = pal[(s, e-1)]
        return table[(s, e)]


print(lps(0, len(myString)-1), pal[0, len(myString)-1])
# print(table)
# print(pal)