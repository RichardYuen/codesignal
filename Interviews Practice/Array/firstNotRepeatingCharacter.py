def firstNotRepeatingCharacter(s):
    count = [0 for i in range(256)]
    for ch in s:
        count[ord(ch)] += 1
    
    for ch in s:
        if count[ord(ch)] == 1:
            return ch
        
    return '_'