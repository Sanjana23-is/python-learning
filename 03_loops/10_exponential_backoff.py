# Q10. Exponential Backoff:
# Double the wait time between retries, starting from 1 second.
# Stop after 5 retries.

import time

wait_time = 1  # initial wait time in seconds
max_retries = 5
attempts =0

while attempts < max_retries:
    print("attempt", attempts+1, "- wait time:", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2  # double the wait time
    attempts += 1