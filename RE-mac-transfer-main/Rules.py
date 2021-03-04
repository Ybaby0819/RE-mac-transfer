def rules_01(MAC_address):
    pass

def rules_02(MAC_address):
    pass

def rules_03(MAC_address):
    pass

def rules_04(MAC_address:list):
    MAC_address_res = MAC_address.copy()
    MAC_address_res[0] = MAC_address[0] | 0x02
    MAC_address_res[2] = MAC_address[2] & 0xfe
    return MAC_address_res

def rules_05(MAC_address):
    MAC_address_res = MAC_address.copy()
    MAC_address_res[0] = MAC_address[0] | 0x02
    MAC_address_res[3] = (MAC_address[3] & 0xfc) + 0x01
    return MAC_address_res

def rules_06(MAC_address):
    MAC_address_res = MAC_address.copy()
    MAC_address_res[0] = MAC_address[0] | 0x02
    MAC_address_res[4] = (MAC_address[2] & 0xef) | 0x10
    return MAC_address_res

def rules_07(MAC_address):
    MAC_address_res = MAC_address.copy()
    MAC_address_res[0] = MAC_address[0] | 0x02
    MAC_address_res[3] = (MAC_address[3] & 0xfc)
    return MAC_address_res

def rules_08(MAC_address):
    MAC_address_res = MAC_address.copy()
    MAC_address_res[0] = MAC_address[0] | 0x02
    MAC_address_res[2] = (MAC_address[2] & 0xfc) + 1
    return MAC_address_res

def rules_09(MAC_address):
    pass

def rules_10(MAC_address):
    pass

def rules_11(MAC_address):
    pass

def rules_12(MAC_address):
    pass