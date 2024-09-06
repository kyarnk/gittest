def fibich(n):
    a = [0, 1]
    for i in range(2, n):
        fibik = a[i-1] + a[i-2]
        a.append(fibik)
    return a
print(fibich(11))
