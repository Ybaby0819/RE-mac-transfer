def output_res(MAC):

    res = []
    for each in MAC:
        res.append((hex(each)[2:]).upper())

    res = '-'.join(res)
    return res