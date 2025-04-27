import time

class MeasureDurationProperty:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, owner):
        if instance is None:
            return self
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = self.func(instance, *args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            print(f"Property '{self.func.__name__}' took {duration:.6f} seconds to execute.")
            return result
        return wrapper()

class MyClass:
    def __init__(self, value):
        self._value = value
    @MeasureDurationProperty
    def value(self):
        time.sleep(1)
        return self._value

obj = MyClass(42)
print("Accessing the 'value' property:")
print(obj.value)