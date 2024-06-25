class Fibonacci:
    def __init__(self):
        self.sequence = [0, 1]

    def generate_sequence(self, n):
        while len(self.sequence) < n:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def get_sequence(self):
        return self.sequence


fib = Fibonacci()
fib.generate_sequence(30)
print(fib.get_sequence())
