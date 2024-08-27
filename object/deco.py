def py(func):
    def wrapper(*args, **kwargs):
        print("python is ", func(*args, **kwargs))
    return wrapper

@py
def free(s):
    return s

@py
def obj():
    return "object"

free("free")
obj()

