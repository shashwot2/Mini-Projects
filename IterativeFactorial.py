def number(n):
  total = 2
  for i in range (2, n):
    total = total + total*i
  return total
  
  
print(number(14))