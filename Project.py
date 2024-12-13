x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum1 = 0
sum2 = 0

for i in range(10):
    sum1 += (x[i] - 2) ** 3   
    sum2 += x[i] ** 2         

S = sum1 + sum2

print("S =", S)
