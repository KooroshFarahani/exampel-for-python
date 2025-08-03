list1 = list(range(1,10))
list2 = list(range(1,10))
list3=list1+list2
print (list3)
for i in list3:
    if i ==5:
        list3[i]=0
        list3.remove(i)
print (list3)
    