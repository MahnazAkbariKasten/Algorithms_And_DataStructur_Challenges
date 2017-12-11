__author__ = 'pretymoon'


def coin2(w, lis):
    k = [0] * (w + 1)
    k[0] = 1
    combo = [[] for i in range(w + 1)]
    combo[0] = [[]]

    for coin in lis:
        for j in range(1, w+1):
            if j >= coin:
                k[j] += k[j - coin]
                for x in combo[j - coin]:
                    y = x.copy()
                    y.append(coin)
                    combo[j].append(y)

    print("combinations: ", combo[w])
    return k[w]

print(coin2(15, [2, 3, 5]))
