n=int(input("Enter number:"))

s=""
for i in range(n):
    val=input()
    s=s+val
max=-99999
for i in range(n):
       val=int(s[i])
       if val > max :
             max=val

max2=-99999            
for i in range(n):
      val=int(s[i])
      if val!=max :
            if val> max2:
                  max2= val
print("second largest:",max2)   