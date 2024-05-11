"""
A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. 
The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool. 
"""
# Simple example

import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker) 
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
