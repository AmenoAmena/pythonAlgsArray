from random import randint

class arrayAlgs:
    def __init__(self):
        pass

    def reverse(self, array):
        if len(array) < 2:
            print("array length should be bigger than 1 tou use this")
        array.reverse()
        return array  

    
    
    def firstLast(self, array):
        lastNumber = len(array) - 1
        if len(array) < 2:
            print("Array length should be bigger than 1 to use this")
        else:
            temp = array[0]
            array[0] = array[lastNumber]
            array[lastNumber] = temp
            return array
            
    
    
    def arrayRoulette(self, array):
        if len(array) <= 1:
            print("Array length should be bigger than 1 to use this")
        else:
            while len(array) > 1:
                randomIndex = randint(0, len(array) - 1)
                del array[randomIndex]
        return array

    
    
    def badThirteen(self, array):
        if len(array) == 0:
            return array
        elif len(array) == 1:
            if array[0] == 13:
                return []
            else:
                return array
        else:
            while 13 in array:
                array.remove(13)
        return array

    def badThirteenSort(self, array):
        if len(array) <= 1:
            print("Array length should be bigger than 1 to use this")
        else:
            while 13 in array:
                array.remove(13)
            array.sort()
        return array

    def killArray(self, array):
        array = None
        return array


arr = arrayAlgs()

