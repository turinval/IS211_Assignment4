import random
import time


def sequential_search(a_list, item):
    """Performs an unordered sequential search and measures execution time."""
    start_time = time.perf_counter()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    elapsed_time = time.perf_counter() - start_time
    return found, elapsed_time


def ordered_sequential_search(a_list, item):
    """Performs an ordered sequential search and measures execution time.

    Assumes a_list is sorted in ascending order.
    """
    start_time = time.perf_counter()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos += 1

    elapsed_time = time.perf_counter() - start_time
    return found, elapsed_time


def binary_search_iterative(a_list, item):
    """Performs an iterative binary search and measures execution time.

    Assumes a_list is sorted in ascending order.
    """
    start_time = time.perf_counter()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    elapsed_time = time.perf_counter() - start_time
    return found, elapsed_time


def binary_search_recursive(a_list, item):
    """Performs a recursive binary search and measures total execution time.

    Uses an index-based helper to prevent slicing overhead. Assumes a_list is sorted.
    """
    start_time = time.perf_counter()

    def _recursive_helper(first, last):
        if first > last:
            return False
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return _recursive_helper(first, midpoint - 1)
        else:
            return _recursive_helper(midpoint + 1, last)

    found = _recursive_helper(0, len(a_list) - 1)
    elapsed_time = time.perf_counter() - start_time
    return found, elapsed_time


def main():
    sizes = [500, 1000, 5000]
    num_trials = 100
    target = 99999999  # Guaranteed worst-case target

    for size in sizes:
        print(f"\n--- Benchmark Results for List Size: {size} ---")

        total_seq = 0.0
        total_ord_seq = 0.0
        total_bin_iter = 0.0
        total_bin_rec = 0.0

        for _ in range(num_trials):
            # Generate random list of positive integers
            test_list = [random.randint(1, 1000000) for _ in range(size)]

            # 1. Unordered Sequential Search
            _, elapsed = sequential_search(test_list, target)
            total_seq += elapsed

            # Sort the list prior to running ordered and binary search algorithms
            test_list.sort()

            # 2. Ordered Sequential Search
            _, elapsed = ordered_sequential_search(test_list, target)
            total_ord_seq += elapsed

            # 3. Binary Search Iterative
            _, elapsed = binary_search_iterative(test_list, target)
            total_bin_iter += elapsed

            # 4. Binary Search Recursive
            _, elapsed = binary_search_recursive(test_list, target)
            total_bin_rec += elapsed

        # Compute averages
        avg_seq = total_seq / num_trials
        avg_ord_seq = total_ord_seq / num_trials
        avg_bin_iter = total_bin_iter / num_trials
        avg_bin_rec = total_bin_rec / num_trials

        # Output results matching exact assignment formatting
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average")
        print(
            f"Ordered Sequential Search took {avg_ord_seq:10.7f} seconds to run, on average"
        )
        print(
            f"Binary Search Iterative took {avg_bin_iter:10.7f} seconds to run, on average"
        )
        print(
            f"Binary Search Recursive took {avg_bin_rec:10.7f} seconds to run, on average"
        )


if __name__ == "__main__":
    main()