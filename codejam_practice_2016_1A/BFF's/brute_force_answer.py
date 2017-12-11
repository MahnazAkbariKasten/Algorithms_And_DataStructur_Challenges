__author__ = 'pretymoon'

import itertools
# The F parameter is the list of BFF identifiers, but 0-based (subtracting 1 from the input).
def cc(F):
  print(F)
  n = len(F)
  r = 0
  # Iterate over all possible orderings of the n kids.
  for O in itertools.permutations(range(n)):
    # print(O)
    first = O[0]
    second = O[1]
    for i in range(1, n):  # Iterate over the permutation, skipping the first.
      # Check if i can be the last one by checking it and the first.
      prev = O[i - 1]
      cur = O[i]
      if ((F[cur] == first or F[cur] == prev) and  ## loop
          (F[first] == cur or F[first] == second)):
        r = max(r, i + 1)
      # Check if i can be in the middle, and stop if it can't.
      if F[cur] != prev and (i == n - 1 or F[cur] != O[i + 1]):
        break
  return r

f=[2, 1, 4, 5, 4, 7, 1]
print(cc([x-1 for x in f]))