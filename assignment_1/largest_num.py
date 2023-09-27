n=int(input("Enter the number:"))
l1=-999999 
for i in range(n):
    val=int(input())
    if val>l1:
        l1=val
print("largest number:",l1)
 