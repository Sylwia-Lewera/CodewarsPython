"""
Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number n of smallest elements to return.

Also:

the number of elements to be returned cannot be higher than the array/list/vector length;
elements can be duplicated;
in case of duplicates, just return them according to the original order (see third example for more clarity).
Same examples and more in the test cases:

first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []

"""
def first_n_smallest(arr, n):
    smallestElements = {}
    temp = arr.copy()
    result = []
    while n > 0:
        smallest = min(arr)
        print('smallest element = ', smallest)
        indexes = [i for i in range(len(temp)) if temp[i] == smallest] 
        print('indexes of smallest:', indexes)
        for idx in indexes:
            if n > 0:
                smallestElements[idx] = smallest
                del arr[idx]
                n -= 1


    print('Smallest elements:', smallestElements)
    sortedByOrder = dict(sorted(smallestElements.items()))
    print('Sorted order:', sortedByOrder)
    for key, value in sortedByOrder.items():
        print('add to results')
        result.append(value)
    return result

print(first_n_smallest([1,2,3,4,5],3))

arrRand = [10, 4, -6, 9, 4, -8, -2, -4, 6, -8, 10, -8, -4, 10, -9, 3, 6, 6, 1, 6, 9, 5, -2, 0, 1, 2, -2, -2, -10, 9, 2, -7, -1, 10, 3, 7, -5]
print('len of rand array: ', len(arrRand))