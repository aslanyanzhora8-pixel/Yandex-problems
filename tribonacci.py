a = 0
b = 1
c = 1


def tribonacci(n):
    global a, b, c
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        i = 2
        if n >= i:
            i += 1
            d = a + b + c
            a = b
            b = c
            c = d
            return a + b + tribonacci(i)


print(tribonacci(3))