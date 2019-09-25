def remove2(lst):
    if len(lst) == 1:
        return lst
    res = remove2(lst[2::])
    res.insert(0, lst[0])
    return res
