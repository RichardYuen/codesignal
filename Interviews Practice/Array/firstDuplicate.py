def firstDuplicate(a):
    seen = [0 for i in range(len(a))]
    for num in a:
        if seen[num-1] != 0:
            return num
        else:
            seen[num-1] += 1
    
    return -1
    