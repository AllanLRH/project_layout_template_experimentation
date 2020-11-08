try:
    from ahrithemetic import my_div, my_mult, my_substract, my_sum
except ImportError:
    print("Failed for direct import")

try:
    from src.ahrithemetic import my_div, my_mult
except ImportError:
    print("Failed for src.-import")

try:
    from .ahrithemetic import my_substract, my_sum
except ImportError:
    print("Failed for dot-import")


def do_advanced_stuff(a, b, c, d, e):
    return my_substract(my_mult(my_sum(my_div(a, b), c), d), e)
