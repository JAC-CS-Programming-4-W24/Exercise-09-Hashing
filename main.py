from __future__ import annotations

from typing import Iterator
from our_dict import Dict
from report import print_table


class our_str:
    """A wrapper class around str to allow us to re-write __hash__"""

    def __init__(self, value: str):
        self._value = value

    # Rule: always implement __eq__ and __hash__ together!
    # Why? Hint: look at our_dict operations
    def __eq__(self, other: our_str) -> bool:
        return self._value == other._value

    def __hash__(self) -> int:
        return 0

    def __getitem__(self, index: int) -> str:
        return self._value[index]

    # Rule: keys should be immutable.
    # Why?
    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        return iter(self._value)


def main():
    # read all names from the file.
    names: list[our_str] = []
    with open("names.txt", "r") as names_file:
        for name in names_file:
            names.append(our_str(name))

    # test our hashing method on different bucket sizes
    for number_of_buckets in [7, 19, 53, 101]:  # why prime? because math.

        # add all the names to the dictionary
        sample: Dict[our_str, int] = Dict(number_of_buckets)
        for name in names:
            sample[name] = 1   # values don't matter for this exercise

        # output the collisions and the "hash evaluation number (1.0 is perfect)"
        print_table(f"Buckets = {number_of_buckets}", sample.bucket_sizes())


if __name__ == "__main__":
    main()
