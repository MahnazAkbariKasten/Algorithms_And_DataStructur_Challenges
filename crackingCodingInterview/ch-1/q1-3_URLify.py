__author__ = 'pretymoon'

def URLify(s):
    # replace spaces with %20
    new_s = s.strip()
    new_s = new_s.replace(" ", "%20")
    return new_s

def URLify_rmExtraSpace(s):
    # reduce the number of adjacent spaces to one
    new_s = s.strip()
    s_ls = []

    for i in range(len(new_s) - 1):
        if not (new_s[i] == new_s[i+1] == " "):
            if new_s[i] == " ":
                s_ls.append("%20")
            else:
                s_ls.append(new_s[i])

    if new_s[-1] == " ":
        s_ls.append("%20")
    else:
        s_ls.append(new_s[-1])

    return "".join(s_ls)

print(URLify("  m    m  "))
print(URLify_rmExtraSpace(" m   m "))

