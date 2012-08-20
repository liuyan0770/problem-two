#import string

a=[[1,2,0,4,5],[2,3,4,8,1],[1,1,5,3,0]]
max=a[0][0]
for i in range(0,2):
    for j in range(0,4):
        sum=a[i][j]+a[i+1][j]+a[i][j+1]+a[i+1][j+1]
        if sum>max:
            max=sum
            m=i
            n=j

def func(m,n):
    print a[m][n],a[m][n+1]
    print a[m+1][n],a[m+1][n+1]

func(m,n)
            


