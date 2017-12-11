__author__ = 'pretymoon'

myString = "tthisisatest"
myDict = {"this", "his", "is", "a", "test"}

l = len(myString)
table = [[-1 for i in range(l)] for j in range(l)]

for i in range(l-1, -1, -1):
    if myString[i:i+1] in myDict:  # if the character in the current position exists in the dictionary, corresponding
                                   # location in the table will be set to ???
        table[i][i] = i
    for k in range(i, l):
        if myString[i:k+1] in myDict:
            table[i][k] = i
            if k < l-1 and table[k+1][l-1] > 0:
                table[i][k+1:] = table[k+1][k+1:]

if table[0][-1] >= 0:
    for i in range(l):
        if table[0][i] >= 0:
            print(myString[table[0][i]:i+1], " ", end='')
else:
    print("NOT A VALID TEXT!")
