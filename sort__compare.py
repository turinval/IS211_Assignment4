import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order.

    :param n: Number of elements in the list
    :return: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    """Sort a list using the insertion sort algorithm and return the elapsed time."""
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

    time_spent = time.time() - start_time
    return time_spent


def gap_insertion_sort(a_list, start, gap):
    """Helper function for shell_sort to perform insertion sort on sublists."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap

        a_list[position] = current_value


def shell_sort(a_list):
    """Sort a list using the shell sort algorithm and return the elapsed time."""
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    time_spent = time.time() - start_time
    return time_spent


def python_sort(a_list):
    """Wrapper function that uses Python's built-in sort and returns the elapsed time."""
    start_time = time.time()
    a_list.sort()
    time_spent = time.time() - start_time
    return time_spent


def main():
    """Benchmark insertion sort, shell sort, and python sort."""
    list_sizes = [500, 1000, 5000]
    num_trials = 100

    for the_size in list_sizes:
        # Benchmark Python Sort
        total_time = 0.0
        for _ in range(num_trials):
            my_list = get_me_random_list(the_size)
            total_time += python_sort(my_list)
        avg_time = total_time / num_trials
        print(f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Benchmark Insertion Sort
        total_time = 0.0
        for _ in range(num_trials):
            my_list = get_me_random_list(the_size)
            total_time += insertion_sort(my_list)
        avg_time = total_time / num_trials
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Benchmark Shell Sort
        total_time = 0.0
        for _ in range(num_trials):
            my_list = get_me_random_list(the_size)
            total_time += shell_sort(my_list)
        avg_time = total_time / num_trials
        print(f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        print("-" * 75)


if __name__ == "__main__":
    main()