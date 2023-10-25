from functools import wraps


def decorator(fn):
    @wraps(fn)
    def wrapper():
        print("start:")
        fn()
        print("end")
    return wrapper


@decorator
def work():
    print("work")


work()

print(work.__name__)
