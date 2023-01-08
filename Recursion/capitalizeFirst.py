# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.



def capitalizeFirst(arr):
    list = []
    if len(arr) < 1:
        return arr
    else:
        list.append(arr[0][0].upper() + arr[0][1:])
        list.extend(capitalizeFirst(arr[1:]))
    return list
