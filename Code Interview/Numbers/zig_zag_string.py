__author__ = 'pretty moon'


def zigzag_shape(input_string, num_of_levels):

    """
    Input: a string input_string, an integer num_of_levels
    Output: The elements of input string in a new order. "num_of_levels" is the number of levels in zig-zag.
    Starting from first position in the string and first level, add the elements of string in the levels periodically.
    Output the elements in levels in order.

    Example: input_string = "smartgirlwins", num_of_levels = 4

    output:
    s            i             s
      m        g    r        n
        a    t        l    i
          r             w


    Observations:
    1. Length of string matters, not content of it.
    2. Step_width in first level is zig = '2*n - 2' and zag = '0'
    3. Step_width for other levels '2' to 'n - 1' has a pattern: zig -= 2 * level and zag += 2 * level
    4. Step_width for last level is zig = '0' and zag = '2*n - 2'
    """
    if num_of_levels < 2 or len(input_string)<= num_of_levels:
        print(input_string)
        return

    zigzag_width = 2 * num_of_levels - 2
    step_width_zig = zigzag_width
    step_width_zag = 0
    string_len = len(input_string)
    step = zigzag_width - 1
    symbol = "|"
    for level in range(num_of_levels):
        idx = level  ## first element for each level comes from corespondent index in the string
        flag = True  ## allows to switch between step_width_zig an step_width_zag
        print(symbol*level, end="")

        while idx < string_len:
            print(input_string[idx], end="")
            if flag:
                if step_width_zig == 0:
                    idx += step_width_zag
                    step = step_width_zag - 1
                else:
                    idx += step_width_zig
                    step = step_width_zig - 1
                flag = False
            else:
                if step_width_zag == 0:
                    idx += step_width_zig
                    step = step_width_zig - 1
                else:
                    idx += step_width_zag
                    step = step_width_zag - 1
                flag = True
            if idx < string_len:
                print(symbol*step, end="")
        step_width_zig -= 2
        step_width_zag += 2
        print()
    print()


def zigzag_order(input_string, num_of_levels):

    """
    Input: a string input_string, an integer num_of_levels
    Output: The elements of input string in a new order. "num_of_levels" is the number of levels in zig-zag.
    Starting from first position in the string and first level, add the elements of string in the levels periodically.
    Output the elements in levels in order.

    Example: input_string = "smartgirlwins", num_of_levels = 4

    s            i             s
      m        g    r        n
        a    t        l    i
          r             w

    output: sismgrnatlirw

    Observations:
    1. Length of string matters, not content of it.
    2. Step_width in first level is zig = '2*n - 2' and zag = '0'
    3. Step_width for other levels '2' to 'n - 1' has a pattern: zig -= 2 * level and zag += 2 * level
    4. Step_width for last level is zig = '0' and zag = '2*n - 2'
    """
    if num_of_levels < 2 or len(input_string)<= num_of_levels:
        print(input_string)
        return

    zigzag_width = 2 * num_of_levels - 2
    step_width_zig = zigzag_width
    step_width_zag = 0
    string_len = len(input_string)

    for level in range(num_of_levels):
        idx = level  ## first element for each level comes from corespondent index in the string
        flag = True  ## allows to switch between step_width_zig an step_width_zag

        while idx < string_len:
            print(input_string[idx], end="")
            if flag:
                if step_width_zig == 0:
                    idx += step_width_zag
                else:
                    idx += step_width_zig
                flag = False
            else:
                if step_width_zag == 0:
                    idx += step_width_zig
                else:
                    idx += step_width_zag
                flag = True
        step_width_zig -= 2
        step_width_zag += 2
    print()

zigzag_shape("smartgirlwins", 4)
zigzag_order("smartgirlwins", 4)
zigzag_shape("abcdefghijklm", 10)
zigzag_order("abcdefghijklm", 10)
