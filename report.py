def print_header(label: str):
    print("* " + label)
    print()
    print("|----------+-----------+----------------------------------------------------|\n" +
          "| Bucket # | Key count | Percent of total                                   |\n" +
          "|----------+-----------+----------------------------------------------------|")


def print_footer():
    print("|----------+-----------+----------------------------------------------------|")


def print_row(bucket: int, amount: int, total: int):
    percent: int = int(100.0 * float(amount) / total)
    print(f"| {bucket:<8} | {amount:9} | {'■' * percent : <50} |")


def print_table(label: str, buckets_lenghts: list[int]):
    print_header(label)

    total: int = sum(buckets_lenghts)
    actual: float = 0.0
    collisions: int = 0

    for i, number_of_keys in enumerate(buckets_lenghts):
        print_row(i, number_of_keys, total)
        collisions += number_of_keys - 1 if number_of_keys > 1 else 0
        actual += (number_of_keys * (number_of_keys + 1)) / 2.0

    print_footer()
    print()

    ideal: float = (float(total) / (2 * len(buckets_lenghts))) * (total + 2 * len(buckets_lenghts) - 1)
    hash_evaluation: float = actual / ideal
    print(f"Collisions: {collisions}")
    print(f"Hash evaluation result: {hash_evaluation}")
    print()


