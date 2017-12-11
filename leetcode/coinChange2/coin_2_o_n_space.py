__author__ = 'pretymoon'

def coin2(w, lis):
    k = [0] * (w + 1)
    k[0] = 1

    for el in lis:
        for j in range(1, w+1):
            if j >= el:
                k[j] += k[j - el]

    return k[w]

print(coin2(16, [2, 3, 5]))
