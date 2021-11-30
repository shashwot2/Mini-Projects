# Converts a list into a number of type string that is (###) ###-#### 
# Solution to https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    b = "("
    for i in range(len(n)):
        
        if i < 3:
            b = b + str(n[i])
        elif i == 3:
            b = b + ")" + " " +str(n[i])
        elif i > 3 and i < 6:
            b = b + str(n[i])
        elif i == 6:
            b = b + "-" + str(n[i])
        elif i > 6:
            b = b + str(n[i])
    return b
    