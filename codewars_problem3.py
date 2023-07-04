# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    if number * -1 > 0: #O(1)
        return 0
    sum = 0
    for i in range(1, number): #O(N)
        if i % 3 == 0: #O(1)
            sum += i #O(1)
        elif i % 5 == 0: #O(1)
            sum += i #O(1)
    return sum

#Time Comp: O(N)
#Space Comp: O(1)