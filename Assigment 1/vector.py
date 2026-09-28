import math


class Vector:

    def __init__(self, entries):
        self.entries = entries

    def mean(self):
        """Return the arithmetic mean of the vector entries."""
        return sum(self.entries) / len(self.entries)

    def demean(self):
        """Return a new vector with the mean subtracted from each entry."""
        mean = self.mean()
        return Vector([x - mean for x in self.entries])

    def std(self):
        """Return the population standard deviation."""
        demeaned = self.demean()
        return math.sqrt(
            sum(x ** 2 for x in demeaned.entries) / len(self.entries)
        )
