'''import os

r,w = os.pipe()
pid = os.fork()

if pid > 0:
    os.close(w)
    print("Parent process is Reading!")
    f=os.fdopen(r)
    print("Parent reading text: ",f.read())



else:
    os.close(r)
    print("Child Process squaring numbers")
    for i in range(1,6):
	oper=str i**2
	res = str.encode(oper)
	os.write(w,res)'''















'''
import os
import threading
import getpass

def worker_thread(id):
    print("Worker Thread {} started".format(id))

def master_thread():
    print("Master Thread started")
    username = getpass.getuser()
    if username == "root":
        print("User has administrative privilege")
        for i in range(3):
            t = threading.Thread(target=worker_thread, args=(i,))
            t.start()
    else:
        print("User does not have administrative privilege")

pid = os.fork()
if pid == 0:
    print("Child Process started")
    t = threading.Thread(target=master_thread)
    t.start()
else:
    print("Parent Process")

'''





















'''

import os
import sys
import time
import array

filename = input("Enter the file name: ")

# Check if file is executable
if not os.access(filename, os.X_OK):
    os.chmod(filename, 0o755)

# Allocate shared memory
shared_array = array.array("i", [0] * 20)

def worker1_process():
    for i in range(0, 20, 5):
        for j in range(i, i + 5):
            shared_array[j] = -1 * shared_array[j]
        time.sleep(0.5)

def worker2_process():
    for i in range(0, 20, 5):
        for j in range(i, i + 5):
            shared_array[j] += 3
        time.sleep(0.5)

pid1 = os.fork()
if pid1 == 0:
    worker1_process()
else:
    pid2 = os.fork()
    if pid2 == 0:
        worker2_process()
    else:
        for i in range(20):
            shared_array[i] = i
        os.waitpid(pid1, 0)
        os.waitpid(pid2, 0)
        print("Final shared array:", shared_array)


'''



















'''
import threading
import time

# Integer array of length 20
array = [i for i in range(20)]

# Semaphore to synchronize access to the array
semaphore = threading.Semaphore(1)

# Counter to keep track of which 5 elements of the array are being processed
counter = 0

def worker_thread1():
    global counter

    while counter < 20:
        # Acquire the semaphore
        semaphore.acquire()

        for i in range(counter, counter + 5):
            array[i] *= -1

        counter += 5
        # Release the semaphore
        semaphore.release()

        # Wait for the other thread to finish processing
        time.sleep(0.1)

def worker_thread2():
    global counter

    while counter < 20:
        # Acquire the semaphore
        semaphore.acquire()

        for i in range(counter, counter + 5):
            array[i] += 3

        counter += 5
        # Release the semaphore
        semaphore.release()

        # Wait for the other thread to finish processing
        time.sleep(0.1)

# Start both worker threads
thread1 = threading.Thread(target=worker_thread1)
thread2 = threading.Thread(target=worker_thread2)

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final array
print(array)


'''












'''
import os
import time
import multiprocessing

# Semaphore to synchronize access to the shared resource
semaphore = multiprocessing.Semaphore(0)

def child1():
    print(f"Child 1 with process ID {os.getpid()} and parent process ID {os.getppid()}")
    time.sleep(1)
    semaphore.release()

def child2():
    print(f"Child 2 with process ID {os.getpid()} and parent process ID {os.getppid()}")
    time.sleep(1)
    semaphore.release()

def child3():
    # Wait for both child 1 and child 2 to finish
    semaphore.acquire()
    semaphore.acquire()

    print(f"Child 3 with process ID {os.getpid()} and parent process ID {os.getppid()}")

# Create 2 child processes from the parent process
process1 = multiprocessing.Process(target=child1)
process2 = multiprocessing.Process(target=child2)
process3 = multiprocessing.Process(target=child3)

process1.start()
process2.start()
process3.start()

# Wait for all child processes to finish
process1.join()
process2.join()
process3.join()

'''















