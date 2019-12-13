def trace_call(func):
    def inner(*args, **kwargs):
        print('Funcao execuada: {} args: {}'.format(func.__name__.args))
        return func(*args, **kwargs)
    return inner

@trace_call
def add(x, y):
    return x + y

if __name__ == "__main__":
    print(add(5, 1))
    