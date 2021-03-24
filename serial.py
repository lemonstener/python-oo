"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        '''start and counter attributes are equal to start parameter specified'''
        self.start = self.counter = start

    def __repr__(self):
        return f'<SerialGenerator start = {self.start} counter = {self.counter}'

    def generate(self):
        '''generate will increase the counter each time it's called and return it'''
        self.counter += 1
        return self.counter - 1

    def reset(self):
        '''reset will change the value of counter to match the one set in start'''
        self.counter = self.start
