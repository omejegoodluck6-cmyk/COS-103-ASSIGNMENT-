"""Basic statistics on a list of numbers: sum, mean, median and mode."""


def list_sum(numbers):
    """Return the sum of the numbers in the list."""
    total = 0
    for n in numbers:
        total += n
    return total


def list_mean(numbers):
    """Return the average (mean) of the numbers in the list."""
    if not numbers:
        raise ValueError("Cannot compute the mean of an empty list.")
    return list_sum(numbers) / len(numbers)


def median_and_mode(numbers):
    """Return a tuple (median, mode) for the numbers in the list.

    If several values tie for most frequent, mode is a list of all of them
    (in ascending order); otherwise it is a single value.
    """
    if not numbers:
        raise ValueError("Cannot compute the median/mode of an empty list.")

    # Median
    ordered = sorted(numbers)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        median = ordered[mid]
    else:
        median = (ordered[mid - 1] + ordered[mid]) / 2

    # Mode
    counts = {}
    for x in ordered:
        counts[x] = counts.get(x, 0) + 1
    highest = max(counts.values())
    modes = [x for x, c in counts.items() if c == highest]
    mode = modes[0] if len(modes) == 1 else modes

    return median, mode


if __name__ == "__main__":
    data = [4, 1, 2, 2, 3, 5, 4, 2]
    print("Numbers:", data)
    print("Sum:    ", list_sum(data))
    print("Mean:   ", list_mean(data))
    median, mode = median_and_mode(data)
    print("Median: ", median)
    print("Mode:   ", mode)
