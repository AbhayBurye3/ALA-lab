import math
from vector import Vector


def test_mean():
    v = Vector([1, 2, 3, 4, 5])
    assert v.mean() == 3


def test_mean_is_translation_invariant():
    v = Vector([1, 2, 3, 4])
    shifted = Vector([11, 12, 13, 14])

    assert shifted.mean() == v.mean() + 10


def test_demean():
    v = Vector([1, 2, 3, 4, 5])

    assert v.demean().entries == [-2, -1, 0, 1, 2]


def test_demean_has_mean_zero():
    v = Vector([2, 4, 6, 8])

    assert math.isclose(v.demean().mean(), 0)


def test_std():
    v = Vector([1, 2, 3, 4, 5])

    assert math.isclose(v.std(), math.sqrt(2))


def test_std_is_nonnegative():
    v = Vector([-5, 0, 5])

    assert v.std() >= 0


def test_std_of_constant_vector_is_zero():
    v = Vector([7, 7, 7, 7])

    assert v.std() == 0


def test_std_is_translation_invariant():
    v = Vector([1, 2, 3, 4])
    shifted = Vector([101, 102, 103, 104])

    assert math.isclose(v.std(), shifted.std())


def test_std_uses_demeaned_values():
    v = Vector([1, 3, 5])

    expected = math.sqrt(8 / 3)

    assert math.isclose(v.std(), expected)
