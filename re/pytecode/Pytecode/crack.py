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
    flag[9] = flag[14] = flag[19] = flag[24] = chr((2441 - sum)/3)
    # flag[9] = flag[14] = flag[19] = '?'

    print flag[21], ord(flag[9]), ''.join(flag)