k = int(input('Enter the value of K: '))
lst = [1,2,3,2,4,5,1]

temp = []
for i in range(len(lst)):
    if(len(temp)==0):
        temp.append(lst[i])
    elif(len(temp)<=k):
        if lst[i] not in temp:
            temp.insert(0,lst[i])
        else:
            var = temp.index(lst[i])
            temp.insert(0 , temp[var])
            temp.pop(var+1)
        if(len(temp) > k):
            temp.pop()
            
print(temp)          

