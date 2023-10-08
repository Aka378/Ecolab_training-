import time

def cached(func):
    dic={}
    def wrapper(num):
        if num in dic.keys():
            return dic[num]
        else:
            result=fact(num)
            dic[num]=result
            return result
    return wrapper        
    
def performance_log(func):
    def wrapper(num):
        start_time = time.time()
        result = func(num)
        end_time = time.time()
        print("time taken:",end_time-start_time)
        print("factorial of",num,result)
    return wrapper        
@cached
@performance_log
def fact(n):
    fn=1
    for i in range(1,n+1):
        fn*=i
    return fn





