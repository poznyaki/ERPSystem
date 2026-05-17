def func1(x):
    return x * 2


print(func1(4))

print(lambda x : x * 2)


print(lambda text, size : text.splitlines()[:size])

def split_size(text, size):
    return text.splitlines()[:size]