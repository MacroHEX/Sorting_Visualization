# import the sorts here
from InsertionSort import insertion_sort

import random
import time

def generate_results(test_list, total_time, sort_type): 
    """
    Takes the information from the test functions and builds the results 
    into a string for readability 

    :param test_list: Python list that is ideally sorted 
    :param total_time: Time object that is total time of the sort 
    :param sort_type: String of the done to get the result
    """

    result_str = ""
    if test_list == sorted(test_list): 
        result_str += "Test: Successful\t"
    else: 
        result_str += "Test: Fail\t"
    
    result_str += "{} sort time: {} seconds".format(sort_type, total_time) 

    return result_str

def test_insertion():
    test_list = [random.randint(0, 1000) for i in range(1000)]

    # time tracking of the sort
    start_time = time.time()
    insertion_sort(test_list, 0, len(test_list) - 1)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Insertion")

    print(result_str)

    return None


def test_selection():
    test_list = [random.randint(0, 1000) for i in range(1000)]

    # time tracking of the sort 
    start_time = time.time()
    selection_sort(test_list, 0, len(test_list) - 1) 
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Selection")

    return None 


def test_bubble():

    pass


def test_merge():

    pass


def test_quick():

    pass


def main():

    # just adding an empty line for readability
    print()

    test_selection()

    test_insertion()

    test_bubble()

    test_merge()

    test_quick()

    print()

    return None


if __name__ == "__main__":
    main()
