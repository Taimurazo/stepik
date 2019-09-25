def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    if b >= a:
        return gcd(a, b % a)


def gcd_while(a, b):
    while a !=0 and b != 0:
        if a > b:
            a = a % b
        if b > a:
            b = b % a
    return a if b == 0 else a


if __name__ == '__main__':
    assert gcd_while(14159572, 63967072) == 4
    assert gcd(35, 18) == 1
