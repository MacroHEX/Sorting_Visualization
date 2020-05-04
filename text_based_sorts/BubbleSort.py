def _swap(test_list, x, y):
    """
    Conducts a Pythonic swap within a list between two indicies 
    Expected Complexity: O(1) (time and space) 

    :param some_list: Python list of integers where the swap will be done 
    :param x: integer of the first index to be swapped with
    :param y: integer of the second index to be swapped with 
    """
    test_list[x], test_list[y] = test_list[y], test_list[x]

def bubble_sort(unsorted): 
    """
    Does a bubble sort given a Python list 
    Expected Complexity: O(n^2) (time) and O(1) (space) 

    :param unsorted: unsorted Python list to be sorted 
    """
    for i in range(len(unsorted)): 
        for j in range(len(unsorted) - 1, i - 1): 
            if unsorted[j] < unsorted[j - 1]: 
                _swap(unsorted, j, j - 1)