# create a way to calculate the power of a number using recursion?
# the way i would do it is by look at this simple power integer 2^4 = 2^2^2^2
# x^a * x^b = x^a+b

def power(base, exp):
    assert int(exp) == exp, "enter only a postive integer"
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / base * power(base, exp+1)
    return base * power(base, exp-1)


print(power(2, -4))
