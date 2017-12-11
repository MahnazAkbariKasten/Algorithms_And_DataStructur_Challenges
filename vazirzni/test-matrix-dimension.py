__author__ = 'pretymoon'

a = [[[() for i in range(4)] for j in range(3)] for k in range(2)] # row:j  col:i  depth:k

for i in range(4): #col
    for j in range(3): #row
        for k in range(2): #depth
            a[k][j][i] = (k, j, i)

# print(a)
# for j in range(3): #col
#     for i in range(4): #row
#         a[0][j][i] = j #[depth][row][col]
# print(a)
for k in range(2):
    print("-"*20)
    for j in range(3):
        print(a[k][j][:])