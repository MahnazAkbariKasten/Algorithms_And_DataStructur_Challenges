__author__ = 'pretymoon'

f = open("\\Mahnaz\\PycharmProjects\\codeJam\\StoreCredit\\storeCreditInput", "r")
numOfCases = int(f.readline())

for i in range(1, numOfCases+1):
    print("Case #%d: " % i, end='')
    credit = int(f.readline())
    numOfItems = int(f.readline())
    strLine = f.readline()
    L = strLine.split(" ")
    priceList = [int(x) for x in L]

    found = 0

    for k in range(0,numOfItems):
        for j in range(k+1,numOfItems):
            if priceList[k]+priceList[j] == credit:
                idx1 = k + 1
                idx2 = j + 1
                found = 1
                break
        if found == 1:
            break

    print(idx1,idx2)


    print("Case #%d: " % i, end='')
    dic = {}
    for idx, price in enumerate(priceList):
        if credit - price in dic:
            result = sorted([idx, dic[credit - price]])
            print(result[0],result[1])
            break
        else:
            dic[price] = idx + 1
        #print(price, dic[price])
    # for price in list(dic.keys()):
    #     curr = dic.pop(price)
    #     if credit - price in dic:
    #         result = sorted([curr, dic[credit - price]])
    #         print(result[0],result[1])
    #         break
