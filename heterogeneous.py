res1=[]
res2=[]
list2=['abc','xyz',1,2,'pqr',3,4,'a']
for j in list2:
    if(type(j)==int):
        res1.append(j)
    elif(type(j)==str):
        res2.append(j)
print("Integer list: " +str(res1))
print("String List: " +str(res2))
