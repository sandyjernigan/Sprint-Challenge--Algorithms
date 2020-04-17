'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    testStr = "th"
    n = len(word)
    
    # Check if test string found in word
    if testStr in word:
        n = word.find("th")
        return count_th(word[n + len(testStr):]) + 1
    else:    
        # Otherwise return 0
        return 0
