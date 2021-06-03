from multiprocessing import Process
import time


start = time.perf_counter()


def do_something(time_for_sleep):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
    print('Done Sleeping...')



p1 = Process(target=do_something, args=[1])
p2 = Process(target=do_something, args=[2])


if __name__ == '__main__':
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2 )} second(s)')