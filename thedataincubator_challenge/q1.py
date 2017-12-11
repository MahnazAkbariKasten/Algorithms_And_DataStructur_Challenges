import itertools
import math
import collections


class CoinsSet:
    def __init__(self, number):
        self.number = number
        self.coins_collection = set(range(1, number+1))
        self.number_of_permutations = math.factorial(self.number)

    def coins_perm_list(self):
        return itertools.permutations(self.coins_collection, self.number)

    # The O(N) implementation is based on some insights on how the payments' components repeat
    def expected_payment_mean(self):
        # For the first coin, you are paid the value of the coin
        payment_sum = sum([i * math.factorial(self.number - 1) for i in range(1, self.number + 1)])

        # For subsequent coins, you are paid the absolute difference between the drawn coin and
        # the previously drawn coin.
        tmp = 0
        for i in range(1, self.number):
            # print("i:", i, "freq:", ((self.number - i)* 2))
            tmp += (self.number - i) * i * 2 * math.factorial(self.number - 2)
        payment_sum += (self.number - 1) * tmp
        print("sum through concise: ", payment_sum)
        return payment_sum / math.factorial(self.number)

    # Implemented the formula
    def payment_std_dev(self):
        dom_cof = self.payment_cof()
        if dom_cof != "TO BE DEVELOPED!":
            pay_mean = self.expected_payment_mean()
            pay_dom = self.payment_domain()
            pay_var = 0
            for mem in pay_dom:
                pay_var += (dom_cof[mem] / self.number_of_permutations) * ((mem - pay_mean) ** 2)
            pay_std_dev = pay_var ** .5
            return pay_std_dev
        else:
            return "TO BE DEVELOPED!"

    # Implemented the formula
    def payment_acum_prob(self, pay_limit):
        dom_cof = self.payment_cof()
        if dom_cof != "TO BE DEVELOPED!":
            pay_dom = self.payment_domain()
            pay_acum_prob = 0
            for mem in pay_dom:
                if mem >= pay_limit:
                                pay_acum_prob += dom_cof[mem] / self.number_of_permutations
            return pay_acum_prob
        else:
            return "TO BE DEVELOPED!"

    def permutation_list(self):
        payments = []

        ###
        print()
        print("for {n} coins, there are {f} permutation."
              .format(n=self.number, f=math.factorial(self.number)))
        tmp = 1
        for member in self.coins_perm_list():
            ###
            if member[0] != tmp:
                print()
                tmp += 1
            print(member, member[0], end=' ')

            payment = member[0]
            for i in range(1, self.number):
                payment += abs(member[i] - member[i-1])
                ###
                print(abs(member[i] - member[i-1]), end=' ')
            ###
            print("payment:", payment)
            payments.append(payment)

        payments.sort()
        cnt = collections.Counter(payments)
        print(dict(cnt))

        ###
        # for key in sorted(cnt):
        #     print(key, "=>", cnt[key], end=" , ")
        # print()
        print("sum through permutation: ", sum(payments))
        print("through permutation: ", sum(payments) / math.factorial(self.number))
        return dict(cnt)

    def payment_domain(self):
        dom = []
        cap = 0
        for i in range(self.number + 1):
            cap += i
        for i in range(self.number, cap+1):
            dom.append(i)
        print(dom)
        return dom

    # This module is not developed yet! Some insights are needed
    # to calculate the frequency of possible payments in the domain
    def payment_cof(self):
        pay_dom = self.payment_domain()

        if self.number <= 10:
            return self.permutation_list()
            # return {10: 1, 11: 1, 12: 10, 13: 12, 14: 64, 15: 84, 16: 312, 17: 432, 18: 1258, 19: 1798, 20: 3836,
            #         21: 5284, 22: 9632, 23: 12772, 24: 20512, 25: 26212, 26: 38197, 27: 47449, 28: 63486, 29: 76548,
            #         30: 96228, 31: 112924, 32: 132828, 33: 151072, 34: 169552, 35: 185104, 36: 198072, 37: 209712,
            #         38: 214784, 39: 219840, 40: 213848, 41: 208992, 42: 197784, 43: 185112, 44: 165348, 45: 147420,
            #         46: 125604, 47: 104292, 48: 83412, 49: 66924, 50: 47952, 51: 36864, 52: 23616, 53: 12672,
            #         54: 8064, 55: 2880}
        else:
            return "TO BE DEVELOPED!"


def make_table():
    ff = open("\\Mahnaz\\PycharmProjects\\thedataincubator_challenge\\dom_cof_in.txt", "r")

    for case in range(10,11):
        strLine = ff.readline()
        pre_a = strLine.replace(" => ", ":").strip()
        a = pre_a.split(" , ")
        dic = {}
        for mem in a:
            key, val = [int(x) for x in mem.split(":")]
            dic[key] = val
        print(dic)

# n_list = [(10, 45), (20, 160)]
# for n in n_list:
#     print("--- N={0} ---".format(n[0]))
#     my_coins = CoinsSet(n[0])
#     # my_coins.permutation_list()
#     print("The expected value for total payment is {0}.".format(my_coins.expected_payment_mean()))
#     # my_coins.payment_domain()
#     print("T standard deviation for total payment is {0}.".format(my_coins.payment_std_dev()))
#     print("The probability that the total payment is greater than or equal to {0} is {1}."
#           .format(n[1], my_coins.payment_acum_prob(n[1])))

my_coins = CoinsSet(3)
my_coins.permutation_list()

