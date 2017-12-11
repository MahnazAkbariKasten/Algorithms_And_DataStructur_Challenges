__author__ = 'prettymoon'

# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.



def mergeKSortedLists(l):

    # Find K, number of lists
    k=len(l)

    # Initialize Indices for lists
    b=()

    sortedList=[]
    # Find one ugly at a time, besides 1.
    while len(ugly) < n:

        # For last ugly found, compute & save uglies for each prime factor.
        for i in range(k):
            l[i].append(primeFactor[i]*ugly[-1])

        # Find & save the next ugly
        ugly.append(min(l[0][0],l[1][0],l[2][0]))

        # Eliminate the last found ugly from the prime factor lists.
        for i in range(3):
            if ugly[-1] == l[i][0]:
                l[i].pop(0)

    print(ugly)


lists= ([54, 60, 64, 72, 80, 90, 96], [54, 60, 72, 75, 81, 90, 96, 108, 120, 135, 144], [60, 75, 80, 90, 100, 120, 125, 135, 150, 160, 180, 200, 225, 240])
sortedLists = mergeKSortedLists(lists)
print(sortedLists)