from typing import TypeVar, Generic

K = TypeVar("K")
V = TypeVar("V")


class Dict(Generic[K, V]):

    def __init__(self, number_of_buckets: int = 19):
        # each bucket is a list of key-value tuples.
        self._buckets: list[list[tuple[K, V]]] = [[] for i in range(number_of_buckets)]
        self._size: int = 0

    def __getitem__(self, search_key: K) -> V:
        # determine the bucket number using the key's hash-code and the % technique from A2
        bucket_number: int = hash(search_key) % len(self._buckets)

        # linear search for the element in the list of colliding keys.
        for key, value in self._buckets[bucket_number]:
            if search_key == key:  # be sure you know why this is == and not comparing hashcodes
                return value

        # key not found --> error
        raise KeyError

    def __contains__(self, search_key) -> bool:
        pass  # code this!

    def __setitem__(self, search_key, value):
        # determine the bucket number using the key's hash-code and the % technique from A2
        bucket_number: int = hash(search_key) % len(self._buckets)

        # linear search for the element in the list of colliding keys.
        i: int = 0
        for key, value in self._buckets[bucket_number]:
            if search_key == key:
                self._buckets[bucket_number][i] = (search_key, value)
                return
            i += 1

        # key not found --> add a new key-value tuple to the list
        self._buckets[bucket_number].append((search_key, value))

    def bucket_sizes(self) -> list[int]:
        """Get the sizes of the buckets to evaluate the performance of the hashing."""
        return list(map(len, self._buckets))
