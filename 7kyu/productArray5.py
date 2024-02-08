"""
Task
Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

Notes
Array/list size is at least 2 .

Array/list's numbers Will be only Positives

Repetition of numbers in the array/list could occur.

Input >> Output Examples
productArray ({12,20}) ==>  return {20,12}
Explanation:
The first element in prod [] array 20 is the product of all array's elements except the first element

The second element 12 is the product of all array's elements except the second element .
"""
def product_array(numbers):
    size = len(numbers)
    prodArray = []    
    for i in range(size):
        newProd = 1
        for j in range(size):
            if j == i:
                continue
            else:
                newProd *= numbers[j]
        prodArray.append(newProd)                    
    return prodArray