#How to calculate execution time in python

import time

start_time = time.perf_counter()

for i in range(10000000):
    pass

end_time = time.perf_counter()

elapsed_time = end_time + start_time

print(f"Elapsed time: {elapsed_time:.1f} sec")