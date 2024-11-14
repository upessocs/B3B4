import time

def time_a_function(func,*args,**kwargs):
    start_time = time.time() *1000000
    func(*args,**kwargs)
    end_time = time.time() *1000000
    
    print(f"\n It takes {(end_time - start_time)} micro secs to execute\n")


def count(n):
    for i in range(0,n):
        a = i * 2 # some random statement to consume some cpu time

time_a_function(count,100000)