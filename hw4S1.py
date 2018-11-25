# Hans Vos
# 10031891
# Due Nov 19
# Homework 4

# Program to test functions a to j.
#
# Define constant variables.

ONE_TEN = [13, 2, 1, 43, 23, 555, 11, 14, 17, 18]

def swapFirstLast(arr):
    arr[0], arr[-1] = arr[-1], arr[0]#1 10 = 10 1
    return arr

def shiftRight(arr):
    arr = [arr[-1]] + arr[:-1]#10 + [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return arr#[10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def replaceEven(arr):
    for index, item in enumerate(arr):
        if item % 2 == 0: # check if element is even
            arr[index] = 0
    return arr

def secondLargest(arr):
    return(sorted(arr, reverse=True)[1])#sorted() method returns a sorted list from the given iterable.
                                        #Setting reverse=True sorts the iterable in the descending order.
                                        #[1]grabs the second number in reverse sorted order

def isIncreasing(arr): # For ascending
    for i in range(len(arr) - 1):#len(range(0, 9)) = 9, if you don't put - 1 the list index will be out of range
        if arr[i] - arr[i+1] > 0:#arr[i]= 1-9, arr[i+1]= 2-10 > 0 (1-2>0 )
            return False
    return True

def hasAdjacentDuplicate(arr):
    return any([i==j for (i, j) in zip(arr, arr[1:])])

def removeMiddle(arr):
    arr.pop((len(arr)-1)//2)#pop removes a specific element at the a specific position
    return arr              #len() Return the length (the number of items) of an object.
                            #// 5.0/2 -> 2.5  5.0//2 -> 2.0

def evenToFront(arr):
    odd  = [n for n in arr if n % 2 != 0]#grabs all odds numbers
    even = [n for n in arr if n % 2 == 0]#grabs all even numbers
    return sorted(even) + sorted(odd)#adds both sorted even and sorted odd numbers to one list

def hasDuplicate(arr):
    return len(arr) != len(set(arr))#length of a list comparing to a length of a list with sets. ex. len(1,2,3)
                                    #does not equal len(sets(1,2,3)) but len(1,2,3,3) does equal to len(sets(1,2,3,3))

def main() :
    print("The original data for all functions is: ", ONE_TEN)
    #a. Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swapFirstLast(data)
    print("After swapping first and last: ", data)
    #b. Demonstrate shifting to the right.
    data = list(ONE_TEN)
    data1 = shiftRight(data)
    print("After shifting right: ", data1)
    # #c. Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replaceEven(data)
    print("After replacing even elements: ", data)
    # #d. Demonstrate replacing values with the larger of their neighbors.
    # data = list(ONE_TEN)
    # replaceNeighbors(data)
    # print("After replacing with neighbors: ", data)
    #e. Demonstrate removing the middle element.
    data = list(ONE_TEN)
    removeMiddle(data)
    print("After removing the middle element(s): ", data)
    #f. Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    evenToFront(data)
    print("After moving even elements: ", evenToFront(data))
    #g. Demonstrate finding the second largest value.
    print("The second largest value is: ", secondLargest(ONE_TEN))
    #h. Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", isIncreasing(ONE_TEN))
    # #i. Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))
    #j. Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))

if __name__=="__main__":
    main()

# The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
# After removing the middle element(s):  [1, 2, 3, 4, 6, 7, 8, 9, 10]
# After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# The second largest value is:  9
# The list is in increasing order:  True
# The list has adjacent duplicates:  False
# The list has duplicates:  False

# The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
# After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
# After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
# After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
# After removing the middle element(s):  [12, 20, 10, 14, 16, 75, 38, 79, 103]
# After moving even elements:  [10, 12, 14, 16, 20, 38, 54, 75, 79, 103]
# The second largest value is:  79
# The list is in increasing order:  False
# The list has adjacent duplicates:  False
# The list has duplicates:  False
#
# The original data for all functions is:  [13, 2, 1, 43, 23, 555, 11, 14, 17, 18]
# After swapping first and last:  [18, 2, 1, 43, 23, 555, 11, 14, 17, 13]
# After shifting right:  [18, 13, 2, 1, 43, 23, 555, 11, 14, 17]
# After replacing even elements:  [13, 0, 1, 43, 23, 555, 11, 0, 17, 0]
# After removing the middle element(s):  [13, 2, 1, 43, 555, 11, 14, 17, 18]
# After moving even elements:  [2, 14, 18, 1, 11, 13, 17, 23, 43, 555]
# The second largest value is:  43
# The list is in increasing order:  False
# The list has adjacent duplicates:  False
# The list has duplicates:  False
