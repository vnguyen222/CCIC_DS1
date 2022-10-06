# GENERATION OF LIST

from random import randint

def GENERATE_LIST(length, range_bounds = [0, 100000]):
    list = []
    for x in range(length):
        list.append(randint(range_bounds[0], range_bounds[1]))
    return list

# unsorted_list = GENERATE_LIST(10, [0, 40])
unsorted_list = [1,64,32,3,4,5,10,34,65,7,8]
print(unsorted_list)

def quicksort(list, start, end):
    if start < end:
        partition_index = partition(list, start, end)
        quicksort(list, start, partition_index - 1)
        quicksort(list, partition_index+1, end)
    
    return list

def partition(list_p, start, end):
    pivot = list_p[end]
    lower_index = start-1
    for x in range(start, end):
        if (list_p[x] < pivot):
            lower_index += 1
            
            # Swap
            temp = list_p[lower_index]
            list_p[lower_index] = list_p[x]
            list_p[x] = temp
    
    # Swap
    temp = list_p[lower_index+1]
    list_p[lower_index+1] = list_p[end]
    list_p[end] = temp

    return lower_index+1



print(quicksort(unsorted_list, 0, len(unsorted_list)-1))