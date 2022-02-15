def divisors(integer):
    arr = []
    for i in range(2, round((integer)/2)+1):
        if integer % i == 0:
            arr.append(i)
    if len(arr) == 0:
        return ("%d is prime"%integer)
    else:
        return arr