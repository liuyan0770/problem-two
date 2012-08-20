#import string

a=raw_input('integer:')
if a[0]=='-':
    print '-',
    if a[len(a)-1]=='0':
        for i in range(1,len(a)-1):
            print a[len(a)-i-1],
    else:
        for i in range(1,len(a)):
            print a[len(a)-i],
elif a[len(a)-1]=='0':
    for i in range(0,len(a)-1):
        print a[len(a)-i-2],
else:
    for i in range(0,len(a)):
        print a[len(a)-i-1],