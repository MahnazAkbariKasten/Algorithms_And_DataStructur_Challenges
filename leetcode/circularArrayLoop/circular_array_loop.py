__author__ = 'pretymoon'
import unittest


class MethodTest(unittest.TestCase):
    def test_mixed_directions(self):
        self.assertFalse(circularArrayLoop([-1, 2, 2]), False)
        self.assertFalse(circularArrayLoop([3, 3, -1, 3, 3]), False)

    def test_forward_loop(self):
        self.assertTrue(circularArrayLoop([2, -1, 1, 2, 2]), True)

    def test_backward_loop(self):
        self.assertTrue(circularArrayLoop([-1, 1, -2, -1]), True)

    def test_short_path(self):
        # self.assertFalse(circularArrayLoop([-1, 2]), False)
        self.assertFalse(circularArrayLoop([3, 1, 2]), True)

def circularArrayLoop(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = len(nums)
        for i in range(s):
            loop_direction = int(nums[i] / abs(nums[i]))
            going = True
            cnt = 0  # number of jumps
            # num_sum = 0  # sum of jump-lengths
            idx = i  # next index after jump
            # print(going, cnt, s, i, idx, nums[idx])
            while going and cnt <= s and nums[idx] != 0:
                cnt += 1
                # num_sum += nums[idx]
                idx = (idx + nums[idx]) % s
                if nums[idx] == 0 or int(nums[idx] / abs(nums[idx])) != loop_direction:
                    going = False
                if going and idx == i:
                    if cnt > 1:
                        # print(cnt)
                        return True
                    else:
                        return False
        return False

if __name__ == "__main__":
    unittest.main()
# print("[2, -1, 1, 2, 2] has a loop? ", circularArrayLoop([2, -1, 1, 2, 2]))
# print("[-1, 2] has a loop? ", circularArrayLoop([-1, 2]))
# print("[3, 3, -1, 3, 3] has a loop? ", circularArrayLoop([3, 3, -1, 3, 3]))
# print("[-1, 3, 3, 4, 2] has a loop? ", circularArrayLoop([-1, 3, 3, 4, 2]))
# def check_for_loop(aray):
#     l = len(aray)
#
#     for i in range(l):
#         path = []
#         loop = False
#         # no_move = True
#         next_idx = (i + aray[i]) % l
#         while next_idx < i:
#             # if aray[i] * aray[next_idx] < 0: # moving back and forth
#             #     no_move = False
#             #     break
#
#
#             path.append(next_idx)
#             next_idx = (next_idx + aray[next_idx]) % l