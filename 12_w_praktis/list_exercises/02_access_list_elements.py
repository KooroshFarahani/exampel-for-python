"""عنصر اول و آخر لیست را چاپ کن"""
list = [1,2,3,4,5,6,7,8,9]
ind=list[0]
list[0]=list[-1] 
list.pop()
list.append(ind)
print(list)
