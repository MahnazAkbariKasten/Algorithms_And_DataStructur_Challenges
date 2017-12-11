__author__ = 'pretymoon'

# http://codercareer.blogspot.com/2012/02/no-32-remove-numbers-in-array.html

def rm_val(val):
    l = 0
    r = len(my_list) - 1
    going = True

    while going:
        while my_list[l] != val and l < r:
            l += 1
        while my_list[r] == val and l < r:
            r -= 1
        if l < r:
            tmp = my_list[l]
            my_list[l] = my_list[r]
            my_list[r] = tmp
            l += 1
            r -= 1
        elif l == r:
            going = False
            return l
        else: # l > r:
            going = False
            return r + 1

my_list = [2, 1, 2, 2, 4, 3, 2, 8]
print(rm_val(2), my_list)