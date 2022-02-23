def isBinary(n):
    a = set(str(n))
    if set(str(n)) == {"0"} or set(str(n)) == {"1"} or set(str(n)) == {"0", "1"} or set(str(n)) == {"1", "0"}:
        return True
    return False
    
def incomplete_virus(s):
    count = 0
    for i in range(1, int(s)+1):
        if isBinary(i):
            count = count + 1
    return count
            
print(incomplete_virus("1000000000000000000"))