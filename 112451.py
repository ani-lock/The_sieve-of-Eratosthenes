def f(z):
    for i in range(2,int(z**0.5)+1):
        if z % i == 0:
            return False
    return True
K, N = map(int,input().split())
B = N
m = [True]*(B+1)
m[0]=m[1]=False
fl = 1
for i in range(2,B+1):
    if m[i]:
        if (K <= i <= B) and (f(2*i+1)):
            fl = 0
            print(i, end = ' ')
        for k in range(i**2,B+1,i):
            m[k] = False
if fl:
    print(0)
