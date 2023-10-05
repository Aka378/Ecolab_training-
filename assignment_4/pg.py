def historgram(List,c,flag):
    for i in List:
           n=List[i]
           m=max(List.values())
           print(i,"",end="|")
           for j in range(m):
                 if(n!=0):
                   print(c,end="")
                   print(" ",end="")
                   n=n-1
                 else:
                      print("   ",end="")
                      print(" ",end="")
           if(flag==True):           
             print(List[i],end=" ")
                    
               
           print()    

l1={2:3,1:3,9:2,4:3,3:6}

historgram(l1,c="---",flag=False)






