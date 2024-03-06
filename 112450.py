B = int(input())
m = [True]*(B+1)
m[0]=m[1]=False
for i in range(2,B+1):
    if m[i]:
        if 2 <= i <= B: print(i, end = ' ')
        for k in range(i**2,B+1,i):
            m[k] = False
        
