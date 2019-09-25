def fibonacci_generator(limit):
    prev = 0
    curr = 1
    while True:
        result = prev + curr
        if result >= limit:
            raise StopIteration
        prev = curr
        curr = result
        yield result


def integers():
    """ Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i += 1


def squares():
    """ Infinite sequence of integer squares."""
    for i in integers():
        yield i * i


def take(number, sequence):
    curr_number = 0
    result = []
    for elem in sequence:
        if curr_number >= number:
            break
        result.append(elem)
        curr_number += 1
    return result


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == '__main__':
    print(fib_recursive(100))
