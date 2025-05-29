import threading
import random
import time

# Flag used to ensure threads start at the same time (more or less)
is_ready = False
target_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
destination_array = []

def threadRacer(threadName):
    """
    The purpose of this function simply put is to pop (remove) the digit currently at index 0 of the target array
    and append it to the destination array.
    """
    global is_ready
    global target_array
    global destination_array

    print(f"Thread {threadName} ready!")
    while not is_ready:
        pass  # Tight spin-wait

    value = target_array.pop(0)
    print(f"Thread {threadName} has value {value}...")
    destination_array.append(value)


def executor():
    global is_ready

    # Prepare threads
    print("Preparing racer threads.")
    threads = []
    for i in range(len(target_array)):
        threadName = f"Thread_{i}"
        t = threading.Thread(target=threadRacer, args=(threadName,))
        threads.append(t)

    for t in threads:
        t.start()

    # Flip the start flag — all threads start racing
    print("All threads ready. Starting...")
    time.sleep(1)
    is_ready = True

    # Close threads
    for t in threads:
        t.join()

    print("Final randomized result:", destination_array)


if __name__ == "__main__":
    executor()
