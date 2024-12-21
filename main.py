class ReverseIterator:
    def __init__(self, iterable, stop=None):
        self.iterable = iterable
        self.index = len(iterable)
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.iterable[self.index]

dig = []
max_value = int(input("Введите число: "))
for i in range(1, max_value + 1):
    dig.append(i)

reverse = ReverseIterator(dig)
for num in reverse:
    print(num)