l = [1, 2, 3, 4, 5]

for i in range(len(l)//2):
    n = l[i]
    l[i] = l[len(l)-1-i]
    l[len(l)-1-i] = n

print(l)
