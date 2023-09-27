min=int(input())
max=int(input())
def prime(n):
    sum=0
    for i in range(1,n+1):
        if n % i == 0:
            sum+=1
    if sum>2:
        return False
    else:
        return True

for i in range(min,max+1):
    if prime(i)==True and i>1:
        print(i)