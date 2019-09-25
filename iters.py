from collections.abc import Iterator


class ReversIterator(Iterator):

    def __init__(self, collection):
        self._collection = collection
        # self._collection.reverse()
        self._collection = self._collection[::-1]
        self.curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < len(self._collection):
            result = self._collection[self.curr] 
            self.curr += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    # l = [1, 2]
    # it = ReversIterator(l)
    # print(next(it)) #0
    # print(next(it)) #1

    l1 = reversed([2,3])

    print(l1)

