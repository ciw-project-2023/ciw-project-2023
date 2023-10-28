from typing import TypeVar, Generator

A = TypeVar('A')


def generate_sublists_largest(input_list: list[A]) -> Generator[list[A], None, None]:
    """Generates all possible combinations of sublist, starting with the longest one."""
    n = len(input_list)
    for size in range(n, 1, -1):
        for i in range(n - size + 1):
            j = i + size
            yield input_list[i:j]
