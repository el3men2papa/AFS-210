import random

def myShuffle(jlist):
    
    
    list_length = len(jlist)
    
    for i in range(list_length):
        
        # generate a random number 
        random_num = random.randint(0, list_length - 1)

        # pop off that random element and add it to the end of the list
        list_element = jlist.pop(random_num)
        jlist.append(list_element)
        
        # pop off the middle number and append it to the end of the list
        mid_point = list_length // 2
        mid_number = jlist.pop(mid_point)
        jlist.append(mid_number)

        # pop off the first number and append it to the end of the list
        first_number = jlist.pop(0)
        jlist.append(first_number)
    
    return jlist

#list of numbert inputed
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