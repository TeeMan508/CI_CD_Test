import logging
import time

from bin import calculate_mean


def main_func():
    logging.info("123321")
    raise AssertionError("ERROR HERE!!!")


if __name__ == "__main__":
    main_func()
