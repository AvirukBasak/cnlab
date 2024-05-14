def bin_divide(num, divisor):
    q, r = '', ''
    n = len(divisor)
    for i in range(len(num)):
        # Division intermediate buffer
        r += num[i]
        # Division length is not reached
        if len(r) < n: continue
        # Quotient based on the first bit of division buffer
        q += '1' if r[0] == '1' else '0'
        # Calculate remainder using XOR operation
        tmp = ''
        tdiv = divisor if r[0] == '1' else '0' * n
        for j in range(n):
            tmp += '1' if (r[j] != tdiv[j]) else '0'
        # Remove leading zeros while len(tmp) > n
        while len(tmp) > n-1 and tmp[0] == '0':
            tmp = tmp[1:]
        r = tmp

    return q, r


def crc(data, divisor):
    n = len(divisor)
    crc_len = n - 1
    padded_data = data + ('0' * crc_len)
    q, r = bin_divide(padded_data, divisor)
    # Pad leading zeros to the remainder
    if len(r) < crc_len:
        r = '0' * (crc_len - len(r)) + r
    return r


data = input("Binary data string (0s & 1s): ")
divisor = input("Binary divisor string (0s & 1s): ")

crc = crc(data, divisor)
print("CRC:", crc)

''' OUTPUT:
Binary data string (0s & 1s): 100100
Binary divisor string (0s & 1s): 1101
CRC: 001
'''
