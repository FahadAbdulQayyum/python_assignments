import time

def measure_duration(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)        
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.6f} seconds to execute.")
        return result
    return wrapper

@measure_duration
def say_hello():
    print("Hello!")

@measure_duration
def simulate_work():
    time.sleep(2)
    print("Work completed!")

say_hello()
simulate_work()