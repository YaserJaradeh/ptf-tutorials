from icecream import ic

from typing import List

Number = int | float


def sum_iteration(lst: List[Number]) -> Number:
    """
    Sum a list of numbers using iteration
    :param lst: the list of numbers
    :return: the sum of the list
    """
    result = 0
    for item in lst:
        result += item
    return result


def sum_recursion(lst: List[Number]) -> Number:
    """
    Sum a list of numbers using recursion
    :param lst: the list of numbers
    :return: the sum of the list
    """
    # stop condition
    if len(lst) == 0:
        return 0
    # recursive call
    return lst[0] + sum_recursion(lst[1:])


###################################################
# Stack View (inverted - the top is at the bottom)
###############
# 1 + sum_recursion([2, 3, 4])
# 1 + (2 + sum_recursion([3, 4]))
# 1 + (2 + (3 + sum_recursion([4])))
# 1 + (2 + (3 + (4 + sum_recursion([]))))
# 1 + (2 + (3 + (4 + 0)))
###################################################


def indirect_recursion_a(n: int):
    """
    Indirect recursion, this one calls another function (b)
    :param n: random number
    :return: nothing
    """
    if n == 0:
        return
    indirect_recursion_b(n - 1)


def indirect_recursion_b(n: int):
    """
    Indirect recursion, this one calls another function (a)
    Dangerous, can cause infinite recursion
    :param n: random number
    :return: nothing
    """
    if n == 0:
        return
    indirect_recursion_a(n - 1)


def tree_recursion(n: int) -> int:
    """
    Tree recursion, this one calls itself multiple times
    This function counts the number of calls (aka. the branches of the tree)
    :param n: how deep the tree is
    :return: the number of calls
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        return tree_recursion(n - 1) + tree_recursion(n - 1)
    return tree_recursion(n - 1) + tree_recursion(n - 1) + tree_recursion(n - 1)


def binary_recursion(n: int) -> int:
    """
    Special case of tree recursion, this one calls itself only twice
    creating a binary tree
    :param n: how deep the tree is
    :return: the number of calls
    """
    if n == 0:
        return 1
    return binary_recursion(n - 1) + binary_recursion(n - 1)


###################################################

paper_graph = {
    "title": "A paper",
    "doi": "1234",
    "abstract": "This is an abstract",
    "authors": ["John", "Jane"],
    "contributions": ["Writing", "Editing"],
    "similar": [
        {
            "title": "Another paper",
            "doi": "5678",
            "abstract": "This is another abstract",
            "authors": ["Rick", "Mick", "Tick"],
            "contributions": ["Reading", "Swimming"],
            "similar": []
        }
    ]
}


def count_authors(paper_dict: dict) -> int:
    """
    Count the number of authors in a paper and all nested papers
    :param paper_dict: the paper represented as a dictionary
    :return: the number of authors
    """
    count = 0
    if "authors" in paper_dict:
        count += len(paper_dict["authors"])
    if "similar" in paper_dict:
        for paper in paper_dict["similar"]:
            count += count_authors(paper)
    return count


if __name__ == '__main__':
    ic(sum_iteration([1, 2, 3, 4]))
    ic(sum_recursion([1, 2, 3, 4]))
    ic(indirect_recursion_a(5))
    ic(tree_recursion(3))
    ic(binary_recursion(3))
    ic(count_authors(paper_graph))
