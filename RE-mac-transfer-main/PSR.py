def psr_01(MAC_address):
    pass


def psr_02(MAC_address):
    MAC = []
    MAC.extend(MAC_address[3:])
    if MAC_address[0] & 0x02:
        hi = MAC[0] >> 2
        hi += 1
        lo = MAC[0] & 0x3
        hi = hi << 2
        MAC[0] = hi | lo
        MAC[1] = MAC_address[4]
        MAC[2] = MAC_address[5]
    else:
        MAC[0] = (MAC_address[3] & 0xfe) | 0x02
        MAC[1] = MAC_address[4]
        MAC[2] = MAC_address[5]

    MAC.extend([0, 0, 0])
    PSR2_MAC = MAC
    return PSR2_MAC
