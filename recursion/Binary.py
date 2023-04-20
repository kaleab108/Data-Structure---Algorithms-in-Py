# how to convert a number from to binary using recursion.
# step 1 recusive case
#   divide number by 2
#   get the quotien for the next iteration
#   get the remainder for the binary digit
#   repeat the steps until the quotient is equal to 0
#
#   f(n)=n mod2+10*f(n/2)
#
# step 2 base case
# step 3 unintentional case
#

def decimalToBinary(n):
    assert n >= 0, 'the number should be a positive integer'
    if n == 0:
        return 1
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


print(decimalToBinary(-11))
