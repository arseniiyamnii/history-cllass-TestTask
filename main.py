from yamniiMod.history.history import history
import random
import time
import sys
from pympler import asizeof

hist = history()
random.seed(version=2)
start_time = time.time()
first_stop_at_MB = 1
second_stop_at_MB = 2
stopper = first_stop_at_MB
filename='arr2.json'
while True:
    sequence=[]
    for i in range(500):
        sequence.append(random.randint(1, 32767))
    hist.set_history(sequence, random.uniform(1,32767))
    if (asizeof.asizeof(hist.history_arr) >= stopper*1024*1024):
        print(hist.history_arr['dupe'])
        print("--- %s seconds ---" % (time.time() - start_time))
        hist.save_history(filename)
        hist.load_history(filename)
        if (stopper != second_stop_at_MB):
            stopper = second_stop_at_MB
        else:
            break


