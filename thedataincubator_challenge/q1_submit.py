__author__ = 'MAHNAZ KASTEN'
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
        # print("sum through concise: ", payment_sum)
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

    def payment_domain(self):
        dom = []
        cap = 0
        for i in range(self.number + 1):
            cap += i
        for i in range(self.number, cap+1):
            dom.append(i)
        return dom

    def permutation_list(self):
        payments = []
        for member in self.coins_perm_list():
            payment = member[0]
            for i in range(1, self.number):
                payment += abs(member[i] - member[i-1])

            payments.append(payment)

        payments.sort()
        cnt = collections.Counter(payments)
        return dict(cnt)

    # This module is not fully developed yet! Some insights are needed
    # to calculate the frequency of possible payments in the domain for large numbers.
    def payment_cof(self):
        pay_dom = self.payment_domain()

        if self.number <= 10:
            # for smaller cases we can find the answer by listing all the permutations
            return self.permutation_list()
        else:
            # for larger cases a simple brute force won't be efficient enough!
            # Paralell computing is an option
            return "TO BE DEVELOPED!"


case_list = [(10, 45), (20, 160), (30, 200)]
for case in case_list:
    print("--- N={0} ---".format(case[0]))
    my_coins = CoinsSet(case[0])
    print("The expected value for total payment is {0}.".format(my_coins.expected_payment_mean()))
    print("The standard deviation for total payment is {0}.".format(my_coins.payment_std_dev()))
    print("The probability that the total payment is greater than or equal to {0} is {1}."
          .format(case[1], my_coins.payment_acum_prob(case[1])))
    print()


# class CoinsSet:
#     def __init__(self, number):
#         self.number = number
#         self.coins_collection = set(range(1, number+1))
#
#     # The O(N) implementation is based on some insights on how the payments' components repeat
#     def expected_payment(self):
#         # For the first coin, you are paid the value of the coin
#         payment_sum = sum([i * math.factorial(self.number - 1) for i in range(1, self.number + 1)])
#
#         # For subsequent coins, you are paid the absolute difference between the drawn coin and
#         # the previously drawn coin.
#         tmp = 0
#         for i in range(1, self.number):
#             tmp += (self.number - i) * i * 2 * math.factorial(self.number - 2)
#
#         payment_sum += (self.number - 1) * tmp
#         return payment_sum / math.factorial(self.number)
#
# n_list = [10, 20, 30]
# for n in n_list:
#     my_coins = CoinsSet(n)
#     print("payments' mean for N={0} is {1}".format(n, my_coins.expected_payment()))
