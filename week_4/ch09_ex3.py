# Write a Python function that uses a for-loop to print the
# number of times each lowercase vowel (a,e,i,o,u) occurs in a
# string s. e.g. "piece" prints "a:0 e:2 i:1 o:0 u:0".

s = "piece"
# check number of e
# count_e = s.count('e')
# print("e:"+str(count_e))

def count_vowels(s):
    # initiate
    count_a = 0
    count_e = 0
    for letter in s:
        if letter == "a":
            count_a += 1
        # if letter == "e":
        elif letter == "e":
            count_e += 1
    # when loop is done
    print("a:"+str(count_a), "e:"+str(count_e))

count_vowels("piece")