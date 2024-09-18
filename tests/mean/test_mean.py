from bin import calculate_mean
from main import main_func


def test_mean():
    assert abs(calculate_mean([1, 2, 3]) - 2.) < 1e-6


# def test_launch_ability() -> None:
#     try:
#         main_func()
#     except Exception as e:
#         assert e is None
