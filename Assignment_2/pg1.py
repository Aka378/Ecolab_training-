l1={}
def freq(List):
    for i in List:
     val=List.count(i)
     l1[i]=val
    for i in l1:
     print(i,l1[i],sep="=")

     
i=[2,2,9,1,2,2,1,4,2,2,3,1]
freq(i)