# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception
# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

# Also provide an equals method, to check that two vectors that have the same components are equal.

class Vector:
    def __init__(self, arr):
        self.arr = arr

    def equals(self, other):
        return all(i == j for i, j in zip(self.arr, other.arr))

    def add(self, other):
        if isinstance(other, __class__):
            if len(other.arr) == len(self.arr):
                res = [i + j for i, j in zip(self.arr, other.arr)]
                return Vector(res)
            else:
                raise Exception('Vectors have different lengths!')
        else:
            raise Exception('Iterable should be a class Vector!')


    def subtract(self, other):
        if isinstance(other, __class__):
            if len(other.arr) == len(self.arr):
                res = [i - j for i, j in zip(self.arr, other.arr)]
                return Vector(res)
            else:
                raise Exception('Vectors have different lengths!')
        else:
            raise Exception('Iterable should be a class Vector!')

    def dot(self, other):
        if isinstance(other, __class__):
            if len(other.arr) == len(self.arr):
                return sum([i * j for i, j in zip(self.arr, other.arr)])
            else:
                raise Exception('Vectors have different lengths!')
        else:
            raise Exception('Iterable should be a class Vector!')

    def norm(self):
        return sum([i ** 2 for i in self.arr]) ** 0.5

    def __str__(self):
        values = ','.join(map(str, self.arr))
        return f"({values})"