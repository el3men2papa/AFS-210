import random

def myShuffle(nlist):
    
    # Time Complexity of this Algorithm: O(n) - Linear Time
    
    list_length = len(nlist)
    
    for i in range(list_length):
        
        # generate a random number based on the size of the list
        random_num = random.randint(0, list_length - 1)

        # pop off that random element and append to the end of the list
        list_element = nlist.pop(random_num)
        nlist.append(list_element)
        
        # pop off the middle number and append it to the end of the list
        mid_point = list_length // 2
        mid_number = nlist.pop(mid_point)
        nlist.append(mid_number)

        # pop off the first number and append it to the end of the list
        first_number = nlist.pop(0)
        nlist.append(first_number)
    
    return nlist

myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print('\nBefore Shuffle:\n')
print(myList)
print('\nShuffled:\n')
print(myShuffle(myList))
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(myShuffle(myList))
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(myShuffle(myList))
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(myShuffle(myList))
myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(myShuffle(myList))
print('\n')