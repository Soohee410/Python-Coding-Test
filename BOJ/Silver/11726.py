n = int(input())

d = [1,2] + [0] * n   #dp table
for i in range(2,n):
    d[i] = (d[i-1] + d[i-2]) % 10007

print(d[n-1])
