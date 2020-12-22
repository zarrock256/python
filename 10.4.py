#Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. Poprawić metodę put() w tablicowej
# implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod testujący kolejkę.

import unittest

class EmptyQueueError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class FullQueueError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

# ------------ Poprawiona metoda get i put: --------------

    def put(self, data):
        if not self.is_full():
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n
        else:
            raise FullQueueError('Kolejka przepełniona!')

    def get(self):
        if not self.is_empty():
            data = self.items[self.head]
            self.items[self.head] = None      # usuwam referencję
            self.head = (self.head + 1) % self.n
            return data
        raise EmptyQueueError('Kolejka jest pusta')

class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        queue = Queue(10)
        self.assertTrue(queue.is_empty())
        queue.put(1)
        self.assertFalse(queue.is_empty())

    def test_isFull(self):
        queue = Queue(1)
        self.assertFalse(queue.is_full())
        queue.put(1)
        self.assertTrue(queue.is_full())

    def test_get(self):
        queue = Queue(10)
        with self.assertRaises(EmptyQueueError):    #sprawdzam, czy odpowiedni wyjątek jest podniesiony
            queue.get()                             #przy próbie pobrania elementu z pustej kolejki
        queue.put(1)
        self.assertEqual(queue.get(),1)

    def test_put(self):
        queue = Queue(2)
        queue.put(1)
        queue.put(1)
        with self.assertRaises(FullQueueError):    #sprawdzam, czy odpowiedni wyjątek jest podniesiony
            queue.put(1)                            #przy przepełnieniu kolejki


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy