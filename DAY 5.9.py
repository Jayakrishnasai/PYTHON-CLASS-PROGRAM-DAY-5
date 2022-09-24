def shuffleArray(a, n):
    i, q, k = 0, 1, n
    while(i < n):     
        j = k 
        while(j > i + q):
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        i += 1
        k += 1
        q += 1
a = [6,9]
n = len(a)
shuffleArray(a, int(n / 2))
for i in range(0, n): 
    print(a[i], end = " ")
