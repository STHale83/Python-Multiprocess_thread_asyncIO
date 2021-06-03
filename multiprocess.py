from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import os
import time

start = time.time()
def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.01)
        #lock.acquire()
        for i in range(len(numbers)):
            with lock:
                numbers[i] +=1
        #lock.release()
#processes = []

#num_processes = os.cpu_count()

#create processes
if __name__ == '__main__':
    lock = Lock()
    #shared_number = Value('i',0)
    shared_array=Array('d',[0.0,100.0,200.0])

    print('Number at beginning is', shared_array[:])
    
    p1 = Process(target = add_100,args=(shared_array,lock))
    p2 = Process(target = add_100,args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is ', shared_array[:])

end = time.time()

print(end - start)