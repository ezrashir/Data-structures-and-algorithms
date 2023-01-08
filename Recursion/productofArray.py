# Write a function called productOfArray which takes in an array of numbers and returns the product of them all.


def productOfArray(arr):
    if len(arr) == 1: 
        return arr[0]
    else:
        return arr[-1] * productOfArray(arr[0:-1])
