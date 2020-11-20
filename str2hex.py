def str2hex(value):
    try:
        return int(value,16)
    except ValueError:
        return 'Invalid MAC address'


def MAC_transfer(MAC_List):
    for i,each_byte in enumerate(MAC_List):
        MAC_List[i] = str2hex(each_byte)
    return MAC_List