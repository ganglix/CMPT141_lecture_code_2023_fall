# CMPT 141 - Sorting Algorithms
# Topic(s): Timing Comparisons

import random as random
import matplotlib.pyplot as plt
import time as time

import cmpt141_sorting_algorithms as cmpt141

def time_sorts( seq ):
    """
    times sorting algorithms from readings on a list of sequences to
    sort data in ascending order.
    seq: sequence to sort
    return: dict of sort times for all sequences in seconds
    """

    sort_times = {'insertion': 0.0, 'mergesort': 0.0, 'quicksort' : 0.0}
    n_times = 10
    # for each sequence, store sort time
    for i in range(n_times):

        # insertion sort
        S = seq.copy()
        time_start = time.time()
        cmpt141.insertion_sort(S)
        sort_times['insertion'] += time.time() - time_start

        # merge sort
        S = seq.copy()
        time_start = time.time()
        cmpt141.merge_sort(S)
        sort_times['mergesort'] += time.time() - time_start

        # quick sort
        S = seq.copy()
        time_start = time.time()
        cmpt141.quick_sort(S)
        sort_times['quicksort'] += time.time() - time_start

    for k in sort_times:
        sort_times[k] = sort_times[k]/n_times

    return sort_times


def sorting_by_size(n_data):
    """
    Run a sorting experiment for the given size.
    :param n_data: how many data items to use in the experiment.
    :return: a dictionary for all three sorts, on 3 kinds of data
    """

    # construct sequences of ints 0 to N-DATA-1 to search
    nums_sorted = [ i for i in range(0,n_data) ]

    nums_reversed = nums_sorted.copy()
    nums_reversed = nums_reversed[::-1]

    nums_random = nums_sorted.copy()
    random.shuffle(nums_random)

    # sorting time performances by algorithm
    times = {}
    times['sorted']   = time_sorts( nums_sorted )
    times['reversed'] = time_sorts( nums_reversed )
    times['random']   = time_sorts( nums_random )

    return times

data = {}
sizes = [50*i for i in range(1,20)]
for scale in sizes:
    data[scale] = sorting_by_size(scale)

#### DISPLAY the results in a nice graphs

# SORTED data
sorted_insertion = [ data[i]['sorted']['insertion'] for i in sizes]
sorted_quick     = [ data[i]['sorted']['quicksort'] for i in sizes]
sorted_merge     = [ data[i]['sorted']['mergesort'] for i in sizes]
plt.figure()
plt.title('Sorted sequences')
plt.xlabel('Sequence size')
plt.ylabel('Time in seconds')
plt.plot(sizes,sorted_insertion)
plt.plot(sizes,sorted_quick)
plt.plot(sizes,sorted_merge)
plt.legend(['insertion sort', 'quicksort', 'mergesort'], loc='best')

# REVERSED SORTED DATA
reversed_insertion = [ data[i]['reversed']['insertion'] for i in sizes]
reversed_quick     = [ data[i]['reversed']['quicksort'] for i in sizes]
reversed_merge     = [ data[i]['reversed']['mergesort'] for i in sizes]

plt.figure()
plt.title('Reverse sorted sequences')
plt.xlabel('Sequence size')
plt.ylabel('Time in seconds')
plt.plot(sizes,reversed_insertion)
plt.plot(sizes,reversed_quick)
plt.plot(sizes,reversed_merge)
plt.legend(['insertion sort', 'quicksort', 'mergesort'], loc='best')


# RANDOM data
random_insertion = [ data[i]['random']['insertion'] for i in sizes]
random_quick     = [ data[i]['random']['quicksort'] for i in sizes]
random_merge     = [ data[i]['random']['mergesort'] for i in sizes]
plt.figure()

plt.title('Random sequences')
plt.xlabel('Sequence size')
plt.ylabel('Time in seconds')
plt.plot(sizes,random_insertion)
plt.plot(sizes,random_quick)
plt.plot(sizes,random_merge)
plt.legend(['insertion sort', 'quicksort', 'mergesort'], loc='best')
plt.show()




# #  https://www.toptal.com/developers/sorting-algorithms
