import time
import random

#region
def quick_sort_partitionFirst(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)

    quick_sort_partitionFirst(a_list, start, pivot-1)
    quick_sort_partitionFirst(a_list, pivot+1, end)
#endregion

#region
def quick_sort_partitionSecond(a_list, start, end):
        # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return
    
    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionSecond(a_list, start, end)

    quick_sort_partitionSecond(a_list, start, pivot-1)
    quick_sort_partitionSecond(a_list, pivot+1, end)
#endregion
    
def quick_sort_partitionLast(a_list, start, end):
        # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return
    
    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionLast(a_list, start, end)

    quick_sort_partitionLast(a_list, start, pivot-1)
    quick_sort_partitionLast(a_list, pivot+1, end)
    
# Last item
def partitionLast(a_list, start, end):
    
    i = (start-1) # index of smaller element
    
    print('a_list: ', a_list)
    
    pivot = a_list[end] # pivot
    
    for j in range(start, end):
    
        # If current element is smaller than or equal to pivot
        if a_list[j] <= pivot:
            
            # increment index of smaller element
            i = i+1
            a_list[i], a_list[j] = a_list[j], a_list[i]
            
    a_list[i+1], a_list[end] = a_list[end], a_list[i+1]
    
    print('a_list: ', a_list)
    
    return partition(a_list, start, end)

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

# Alternate Piviot Points ---------------------

# Second item (used in the instructional video)
def partitionSecond(a_list, start, end):
    if start < end:
        a_list[start], a_list[start+1] = a_list[start+1], a_list[start]
    return partition(a_list, start, end)

#region
    
def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high

#endregion

#print("Quick Sort:")

#myList = [54,26,93,17,77,31]

#myList = [x for x in range(1000)]
#random.shuffle(myList)

#print(myList)

#start_time = time.time()
#quick_sort_partitionFirst(myList,0,len(myList)-1)
#end_time = time.time()

#print()
#print("Sorted Listed: ")
#print(myList)   

#print(f"The execution time for Quick Sort Partition First is: {end_time-start_time}")

# ------------------------------------------

#myList = [x for x in range(1000)]
#random.shuffle(myList)

#start_time = time.time()
#quick_sort_partitionSecond(myList,0,len(myList)-1)
#end_time = time.time()

#print(f"The execution time for Quick Sort Partition Second is: {end_time-start_time}")

# ------------------------------------------

#myList = [x for x in range(1000)]
#random.shuffle(myList)

myList = [54,26,93,17,77,31]

start_time = time.time()
quick_sort_partitionLast(myList,0,len(myList)-1)
end_time = time.time()

print(f"The execution time for Quick Sort Partition Last is: {end_time-start_time}")