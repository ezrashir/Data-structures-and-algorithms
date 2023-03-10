# Write a recursive function called someRecursive which accepts an array and a callback. The function returns true if a single value in the array returns true when passed to the callback. Otherwise it returns false.


def isOdd(num):
    if num%2==0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if len(arr)==1:
        x=cb(arr[0])
        return x
    else:
        if cb(arr[0]) is False:
            return someRecursive(arr[1:], isOdd)
        else:
            return True
