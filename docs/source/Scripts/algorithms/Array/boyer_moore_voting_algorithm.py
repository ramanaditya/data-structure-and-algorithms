def boyer_moore_voting_algorithm(arr: list) -> int:
    """
    :param arr: list
    :return: int
    """
    res = arr[0]  # Initialization
    counter = 0  # Counter

    for i in range(len(arr)):
        if counter == 0:
            res = arr[i]
            counter = 1
        elif res == arr[i]:
            counter += 1
        else:
            counter -= 1

    return res
