import time
def time_a_function(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start_time = time.time() *1000000
        func(*args,**kwargs)
        end_time = time.time() *1000000
        
        print(f"\n It takes {(end_time - start_time)} micro secs to execute\n")
    return wrapper

@time_a_function
def count(n):
    for i in range(0,n):
        a = i * 2 # some random statement to consume some cpu time

# wrapped = time_a_function(count)
# wrapped(1000000)

count(10000)