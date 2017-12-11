__author__ = 'pretymoon'
# 1) Given two words, find if second word is the round rotation of first word.
# For example: abc, cab
# return 1
# since cab is round rotation of abc
#
# Example2: ab, aa
# return -1
# since aa is not round rotation for aa
#
# 2) Given two hexadecimal numbers find if they can be consecutive in gray code
# For example: 10001000, 10001001
# return 1
# since they are successive in gray code
#
# Example2: 10001000, 10011001
# return -1
# since they are not successive in gray code.

def cons(n1, n2):
    bn1 = "".join(["{0:04b}".format(int(c, 16)) for c in n1])
    bn2 = "".join(["{0:04b}".format(int(c, 16)) for c in n2])
    print("bn1: {0} -- bn2: {1}".format(bn1, bn2))
    # res = bin(int(bn1)) ^ bin(int(bn2))
    # if int(bn1, 2) - int(bn2, 2) in {1, -1}:
    if int(n1, 16) - int(n2, 16) in {1, -1}:
        return 1
    return -1

n1 = "f"
n2 = "10"

print("{0} and {1} bitwise comparison: ".format(n1, n2), cons(n1, n2))


def rr(w1, w2):
    tmp = w1
    for i in range(len(w1) - 1):
        tmp = tmp[1:] + tmp[0]
        if tmp == w2:
            return 1
    return -1

w1 = "abcd"
w2 = "dabc"
print("\"{0}\" and \"{1}\" word comparison: ".format(w1, w2),rr(w1, w2))

####################################################
# transpose a matrix
####################################################
m = [[1,2,3],[4,5,6],[7,8,9],[1,1,1]]
n=[]

for i in range(len(m[0])):
    n.append([x[i] for x in m])

print(m,"\n", n)