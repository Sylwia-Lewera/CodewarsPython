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
        smallest = min(arr) # find smallest element, can ooccur multiple times
        indexes = [i for i in range(len(temp)) if temp[i] == smallest] # saving order of smallest values
        for idx in indexes:
            if n > 0:
                smallestElements[idx] = smallest #creating dictionary with smallest elements and their order
                arr.remove(smallest) #removing smallest elements of specified value
                n -= 1
    sortedByOrder = dict(sorted(smallestElements.items())) # sorting n smallest elements in their original order
    for key, value in sortedByOrder.items():
        result.append(value) # adding smallest elements values to the results list in original order
    return result