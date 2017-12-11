__author__ = 'pretymoon'
import collections

ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1B\\A-phone-number\\A-large.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    s = a[0].strip()

    # my_dict = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
    cnt = collections.Counter()
    # table = [[-1 for i in range(11)] for j in range(len(s))]
    phone = []

    for i in range(len(s)):  # count the number of appearance for each letter in the string
        cnt[s[i:i+1]] += 1
    # print(cnt)

    if cnt["Z"]>0:  # use greedy paradigm to distinguish the numbers in the order that works
        phone.append([0]*cnt["Z"])
        cnt["E"] -= cnt["Z"]
        cnt["R"] -= cnt["Z"]
        cnt["O"] -= cnt["Z"]
        cnt["Z"] = 0
    if cnt["W"]>0:
        phone.append([2]*cnt["W"])
        cnt["T"] -= cnt["W"]
        cnt["O"] -= cnt["W"]
        cnt["W"] = 0
    if cnt["U"]>0:
        phone.append([4]*cnt["U"])
        cnt["F"] -= cnt["U"]
        cnt["R"] -= cnt["U"]
        cnt["O"] -= cnt["U"]
        cnt["U"] = 0

    if cnt["X"]>0:
        phone.append([6]*cnt["X"])
        cnt["S"] -= cnt["X"]
        cnt["I"] -= cnt["X"]
        cnt["X"] = 0
    if cnt["G"]>0:
        phone.append([8]*cnt["G"])
        cnt["E"] -= cnt["G"]
        cnt["I"] -= cnt["G"]
        cnt["H"] -= cnt["G"]
        cnt["T"] -= cnt["G"]
        cnt["G"] = 0
    if cnt["O"]>0:
        phone.append([1]*cnt["O"])
        cnt["E"] = cnt["E"] - cnt["O"]
        cnt["N"] = cnt["N"] - cnt["O"]
        cnt["O"] = 0
    if cnt["T"]>0:
        phone.append([3]*cnt["T"])
        cnt["H"] -= cnt["T"]
        cnt["R"] -= cnt["T"]
        cnt["E"] -= 2 * cnt["T"]
        cnt["T"] = 0
    if cnt["S"]>0:
        phone.append([7]*cnt["S"])
        cnt["N"] -= cnt["S"]
        cnt["V"] -= cnt["S"]
        cnt["E"] -= 2 * cnt["S"]
        cnt["S"] = 0
    if cnt["V"]>0:
        phone.append([5]*cnt["V"])
        cnt["F"] -= cnt["V"]
        cnt["I"] -= cnt["V"]
        cnt["E"] -= cnt["V"]
        cnt["V"] = 0
    if cnt["I"]>0:
        phone.append([9]*cnt["I"])
        cnt["N"] -= 2 * cnt["I"]
        cnt["E"] -= cnt["I"]
        cnt["I"] = 0

    # print(phone)
    res = []
    for i in phone:
        res += i
    # print(res)
    for i in sorted(res):
        print(i, end='')
    print()
