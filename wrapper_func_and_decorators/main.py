# Write a function to count n and evaluate a = n * 10 for all values from 0 to n 
import time


def count(n):
    for i in range(0,n):
        a = n * 10


ns = [100000 ,234234 , 34345 ,345,344, 345]
# n = 100000

def wrapper(func,n):
    # code to evalute run time of function call count(n)
    start_time = time.time() * 1000000
    # print(start_time)
    func(n)# timing this function call/execution
    end_time = time.time() * 1000000
    # print(end_time)

    print(f"\n n ={n}Time to execute is {end_time - start_time} micro seconds\n")


for n in ns:
    wrapper(count,n)