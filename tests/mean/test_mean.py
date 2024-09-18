from bin import calculate_mean


def test_mean():
    assert abs(calculate_mean([1, 2, 3]) - 2.) < 1e-6


