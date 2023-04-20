

def factorial(num):
    assert int(num) >= 0, "the number should be a positive integer"
    if num in [0, 1]:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(-4))
