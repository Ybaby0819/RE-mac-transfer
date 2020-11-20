from str2hex import MAC_transfer

#传入ra0参数获取br-lan
def get_br_lan(ra0):


    ra0 = MAC_transfer(ra0)

    #处理阶段，得到br-lan地址：这部分采用最简单的算法，ra0+1即可
    last_byte = ra0[-1] + 1
    br_lan = ra0
    br_lan[-1] = last_byte
    return br_lan