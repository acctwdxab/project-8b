# Dan Wu
# 11/18/2020
# Write a function that takes two strings as parameters and returns a set of the words contained in both strings.

def words_in_both(s1, s2):
 """Take two strings and return a set of words contained in both strings"""
 common_one = s1.lower().split(" ")
 common_two = s2.lower().split(" ")
 result = []
 for words in common_one:
    if (words in common_two) and (words not in result):
        result.append(words)
 return set(result)



