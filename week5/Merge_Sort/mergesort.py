def mergeSort(nlist):

    print("Splitting ", nlist)

    # insert your code to complete the mergeSort function

    list_length = len(nlist)

    if list_length == 1:
        return nlist

    mid_point = list_length // 2

    left_side = mergeSort(nlist[:mid_point])

    right_side = mergeSort(nlist[mid_point:])

    nlist = merge(nlist, left_side, right_side)
    
    print("Merging ", nlist)
    
    return nlist

#List provided to be split
myList = [ 55, 31, 26, 20, 63, 7, 51, 74, 81, 40 ]

#It will determin the lengh of the list to split them by right and left
def merge(nlist, lefthalf, righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

#it will split the lefthalf of the list
    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1


#it will split the right side of the list
    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist



mergeSort(myList)

print('Sorted: ', myList)