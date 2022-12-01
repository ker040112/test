def sorts(list) : 
    if len(list) < 2:
        return list
    
    mid = len(list)//2
    l_list = sorts(list[:mid])
    h_list = sorts(list[mid:])

    merged = []
    l = h = 0
    while l < len(l_list) and h < len(h_list):
        if l_list[l] < h_list[h]:
            merged.append(l_list[l])
            l += 1
        else:
            merged.append(h_list[h])
            h += 1
    merged += l_list[l:]
    merged += h_list[h:]
    return merged