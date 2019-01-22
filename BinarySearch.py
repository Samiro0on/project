# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# binary search 16/1/2019  , divide and conquer

import random
def sortedList (size = 10, max = 100):
    sortedArray = []
    for nTimes in range(0,size):
        sortedArray.append(random.randrange(0,max,1))
    sortedArray.sort()
    return sortedArray
# print(sortedList())

def BinarySearch (sortedArray , goal):

    if len(sortedArray) == 0 or len(sortedArray) == 1 and sortedArray[0] != goal :
        return False

    middleIndex = int(len(sortedArray)/2)
    middleValue = sortedArray[middleIndex]

    if middleValue == goal :
        location = middleIndex
        return True
    if middleValue > goal :
        return BinarySearch(sortedArray[:middleIndex], goal)
    if middleValue < goal :
        return BinarySearch(sortedArray[middleIndex:],goal)


var = sortedList(20,25)
print(var)
print("Did y find yr target = ", BinarySearch(var, goal=23))
