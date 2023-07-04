# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces. 

def get_count(sentence):
    vowels = 'aeiou' #O(1)
    count = 0 #O(1)
    for letter in sentence: #O(N)
        if letter in vowels: #O(1)
            count+= 1 #O(1)
    return count

#Time Comp: O(N)
#Space Comp: O(1)
####################################################################
# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    for letter in string_: #O(N)
        if letter in 'aeiouAEIOU': #O(1)
            string_ = string_.replace(letter,'') #O(N)
    return string_

#Time Comp: O(N**2)
#Space Comp: O(N)
###################################################################

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
######################################################
import random
def create_show(fireworks, show_time):
    fireworks.sort() #O(NlogN)
    show = [] #O(1)
    remaining_time = show_time #O(1)
    while remaining_time > 0 and fireworks: #O(N)
           # Select a random firework
           firework = random.choice(fireworks)
           if firework <= remaining_time: #O(1)
               # Add the firework to the show
               show.append(firework) #O(1)
               remaining_time -= firework #O(1)
           else:
              # This firework is too long, remove it from consideration
              fireworks.remove(firework) #O(N)
    return show

#Time Comp: maybeeee O(N**2)
#Space Comp: #O(N)