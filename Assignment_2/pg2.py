
def historgram(List):
    for i in List:

           print(i,"",end="|")
           for j in range(List[i]):
                 for i in range(4):
                       print("+",end="")
                 print(" ",end="")
               
           print()    

l1={2:3,1:3,9:2,4:3,3:6}

historgram(l1)

