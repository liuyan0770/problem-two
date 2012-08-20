#import string

mark=1 #define a mark and value of 1
mylist=["at","","","","ball","car","","","","","dad","",""] #define a list named mylist
print mylist #print mylist
find=raw_input("input:") #input a string and assign to find
while mark: #judge mark value    
    for i in range(0,len(mylist)): #make i in between 0 to len(mylist) cycles
        if find==mylist[i]: #judge find and mylist[i] equal or not
            print i #print the current value of i
            mark=0  #make mark equal to 0
            break   #end the circulation
        elif i==len(mylist)-1:#judge i and len(mylist)-1 equal or not
            mark=0  #make mark equal to 0
            print '-1' #print '-1'
        else:
            continue # continue for the next round of the cycle



