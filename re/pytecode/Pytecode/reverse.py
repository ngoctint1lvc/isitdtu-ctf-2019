def Ch3cking(flag):
    check = 0
    if (ord(flag[0]) + 52) != ord(flag[-1]):
        F4ll()
        return None
    if (ord(flag[-1]) - 2) != ord(flag[7]):
        F4ll()
        return None
    if flag[:7] != 'ISITDTU':
        sys.exit(0)
    if (flag[9] != flag[14]) or (flag[14] != flag[19]) or (flag[19] != flag[24]):
        check += 1
        return None
    if (ord(flag[8]) != 49) or (flag[8] != flag[16]):
        F4ll()
        return None
    if flag[10:14] != 'd0nT':
        check += 1
        return None
    if (int(flag[18]) + int(flag[23]) + int(flag[28])) != 9:
        F4ll()
        return None
    if flag[18] != flag[28]:
        F4ll()
        return None
    if flag[15] != 'L':
        check += 1
        return None
    if (ord(flag[17]) ^ -10) != -99:
        F4ll()
        return None
    if (ord(flag[20]) + 2) != ord(flag[27]):
        check += 1
        return None
    if ord(flag[27]) > 123:
        check += 1
        return None
    if ord(flag[20]) < 97:
        check += 1
        return None
    if (ord(flag[27]) % 100) != 0:
        F4ll()
        return None
    if flag[25] != 'C':
        check += 1
        return None
    if (ord(flag[26]) % 2) != 0:
        F4ll()
        return None
    if (ord(flag[26]) % 3) != 0:
        F4ll()
        return None
    if (ord(flag[26]) % 4) != 0:
        F4ll()
        return None
    if not flag[26].isdigit():
        F4ll()
        return None
    if int(flag[23]) != 3:
        check += 1
        return None
    if flag[22] != flag[13].lower():
        F4ll()
        return None
    if check:
        F4ll()
        return None
    tmp = 0
    for i in flag:
        tmp += ord(i)
    if tmp != 2441:
        F4ll()
        return None
    C0rr3ct()
    return True

def C0rr3ct():
    pass

def F4ll():
    pass

import string

# flag[0] + 52 == flag[-1]
# flag[9] = flag[14] = flag[19] = flag[24]
# flag[18] = flag[28]
flag = ['.']*30

flag[:7] = 'ISITDTU'
flag[10:14] = 'd0nT'
flag[15] = 'L'
flag[17] = chr(-99 ^ -10)
flag[27] = chr(100)
flag[25] = 'C'
flag[26] = '0'
flag[23] = '3'
flag[22] = flag[13].lower()
flag[-1] = chr(ord(flag[0]) + 52) # flag[29] = }
flag[7] = '{'
flag[8] = chr(49)
flag[16] = flag[8]
flag[20] = chr(ord(flag[27]) - 2)
flag[18] = flag[28] = '3' # flag[18] + flag[28] + flag[23] = 9

for ch in string.printable:
    # flag[21] = 'Y'
    flag[21] = ch
    sum = 0
    for i in range(len(flag)):
        if i not in [9, 14, 19, 24]:
            sum += ord(flag[i])
    flag[9] = flag[14] = flag[19] = flag[24] = chr((2441 - sum)/4)
    # flag[9] = flag[14] = flag[19] = '?'

    print flag[21], Ch3cking(''.join(flag)), ''.join(flag)

