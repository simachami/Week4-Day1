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