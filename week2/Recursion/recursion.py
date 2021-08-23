def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1rec(i,odd_sum):
    # Duplicate the loop1 function using recursion
    if i >= 20:
        return odd_sum
    elif (i % 2) == 1:
        odd_sum += i
    return loop1rec(i+1,odd_sum)

def loop2Rec(i,even_sum):
    # Duplicate the loop2 function using recursion
    if i == 20:
        return even_sum
    elif (i % 2) == 0:
        even_sum += i
    i += 1
    return loop2Rec(i+1,even_sum)


print('Sum of odds between 1 and 20 using for loop =',loop1())
i=0
odd_sum=0

print('Sum of odds between 1 and 20 using recursion =',loop1rec(i,odd_sum))

print('Sum of evens between 1 and 20 using while loop =',loop2())
i=0
even_sum=0

print('Sum of evens between 1 and 20 using recursion =',loop2Rec(i,even_sum))