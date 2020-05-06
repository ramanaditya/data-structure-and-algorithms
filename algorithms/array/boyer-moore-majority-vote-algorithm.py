"""
Boyer–Moore majority vote algorithm
Reference : https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

Description : To find the majority element from the sequence, majority means the element should be present more than n/2
times the total length of the sequence.
If the no such element occurs, then algorithm can return any arbitrary element, that is not guaranteed that this element
will be the mode or occurred maximum number of times.

Linear TIme
Constant Space
"""


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
