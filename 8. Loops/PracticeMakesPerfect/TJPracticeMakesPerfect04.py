
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


print (digit_sum(1234))
