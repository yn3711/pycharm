class MyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Hi I'm MyError!"

try:
    raise MyError()
except Exception as e:
    print(e)  # "Hi I'm MyError!"" と出力される