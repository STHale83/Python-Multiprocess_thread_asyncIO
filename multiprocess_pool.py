from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue
import os
import time



def cube(number):
    return number*number*number


if __name__ == '__main__':
    start = time.time()
    
    numbers = range(10)

    pool = Pool()

    # map, apply, join, close

    result = pool.map(cube,numbers)
    # pool.apply(cube,numbers[0])
    pool.close()

    pool.join()

    end = time.time()

    print(end - start)
    print(result)