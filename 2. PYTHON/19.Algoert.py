##An algorithm is a series of steps to complete a given task or solve a problem. On a day-to-day basis, 
# you use algorithms all the time to complete tasks
def isPalindrome(str):
    starIndex = 0
    endIndex = len(str)-1

    print(starIndex)

    for x in str:
        if str[starIndex] != str[endIndex]:
            return False
    return True

print (isPalindrome('rececar'))            