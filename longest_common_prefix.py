strs=["flower","flow","flight","flourish","flame"]  
strf=[]
for j in range(len(strs[0])):
    count=0
    found=True
    for i in range(1,len(strs)):
        if j>=len(strs[i]) or strs[0][j]!=strs[i][j]:  
            found=False
            break          
        else:
            count+=1
    if count==(len(strs)-1):
        strf.append(strs[0][j])
    
    if found==False:
        break
if len(strf)==0:
    result=[""]
else:                                   
    result=["".join(strf)]
print(result)

