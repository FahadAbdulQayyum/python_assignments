import time

class MeasureDuration:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{self.func.__name__}' took {duration:.6f} seconds to execute.")
        return result

@MeasureDuration
def say_hello():
    print("Hello!")
@MeasureDuration
def simulate_work():
    time.sleep(2)
    print("Work completed!")

say_hello()
simulate_work()