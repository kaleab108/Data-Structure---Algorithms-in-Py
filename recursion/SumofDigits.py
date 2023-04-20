# write out the method of how to find the sum of digits of  a positive nteger number using Recursion?
# f(n) = n/10 + n/10
# add assert to have intgers as an input

def sumofDigits(n):
    assert n >= 0 and int(
        n) == n, 'the number has to be a positive integer only'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n/10))


print(sumofDigits())
