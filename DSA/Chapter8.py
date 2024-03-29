# 1.  Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].

def intersect(array1, array2):
    array3 = []
    hash_table = {}
    
    for i in array1:
        hash_table[i] = True
        
    for i in array2:
        if i in hash_table:
            array3.append(i)
    
    return array3

arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]
print(intersect(arr1, arr2))


# 2. Write a function that accepts an array of strings and returns the first duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], the function should return "c", since it’s duplicated within the array.
def duplicate_value(array):
    hash_table = {}
    
    for number in array:
        if number in hash_table:
            return number
        else:
            hash_table[number] = True
            
array = ["a", "b", "c", "d", "c", "e", "f"]
print(duplicate_value(array))


# 3. Write a function that accepts a string that contains all the letters of the alphabet except one and returns the missing letter. For example, the string, "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet except the letter, "f".

def missing_letter(phrase):
    hash_table = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        hash_table[letter] = True
    
    for letter in phrase.lower():
        if letter in hash_table:
            return letter
    
print(missing_letter("The quick brown box jumps over a lazy dog"))


# 4. Write a function that returns the first non-duplicated character in a string. For example, the string, "minimum" has two characters that only exist once—the "n" and the "u", so your function should return the "n", since it occurs first.

def non_dupe(word):
    hash_table = {}

    for letter in word.lower():
        if letter in hash_table:
            hash_table[letter] += 1
        else:
            hash_table[letter] = 1
    
    for letter in word.lower():
        if hash_table[letter] == 1:
            return letter
        
print(non_dupe("minimum"))