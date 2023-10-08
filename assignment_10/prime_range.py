class PrimeRange:
    def _init_(self, start, end=None):
        if end is None:
            self.start = 2
            self.end = start
        else:
            self.start = start
            self.end = end

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def _iter_(self):
        return self

    def _next_(self):
        current = self.start
        while current <= self.end:
            if self.is_prime(current):
                self.start = current + 1
                return current
            current += 1
        raise StopIteration()

def prime_range(*args):
    if len(args) == 1:
        return PrimeRange(2, args[0])
    elif len(args) == 2:
        return PrimeRange(args[0], args[1])
    else:
        raise ValueError("invalid arguments")
