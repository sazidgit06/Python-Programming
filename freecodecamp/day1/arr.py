def find_missing_numbers(arr):
    if len(arr) == 0:
        return []

    num_set = set(arr)
    max_val = max(arr)
    missing = []

    for i in range(1, max_val + 1):
        if i not in num_set:
            missing.append(i)

    return missing