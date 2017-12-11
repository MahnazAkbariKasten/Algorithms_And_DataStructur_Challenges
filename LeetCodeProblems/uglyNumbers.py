__author__ = 'prettymoon'

# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note that 1 is typically treated as an ugly number.

# Initialize the number of uglies you want to find.


def findUglyNumbers(n):

    # Initialize the uglies' list with 1.
    ugly=[1]

    # Tuple of valid prime factors
    primeFactor=(2,3,5)

    # Define tuple for list of uglies, one list for each prime factor
    l=([],[],[])

    # Find one ugly at a time, besides 1.
    while len(ugly) < n:

        # For last ugly found, compute & save uglies for each prime factor.
        for i in range(3):
            l[i].append(primeFactor[i]*ugly[-1])

        # Find & save the next ugly
        ugly.append(min(l[0][0],l[1][0],l[2][0]))

        # Eliminate the last found ugly from the prime factor lists.
        for i in range(3):
            if ugly[-1] == l[i][0]:
                l[i].pop(0)

    print(ugly)


n=25
findUglyNumbers(n)