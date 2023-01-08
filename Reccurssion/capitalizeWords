Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.


def capitalizeWords(arr):
    list = []
    if len(arr)<1:
        return arr
    else:
        list.append(arr[0].upper())
        list.extend(capitalizeWords(arr[1:]))
    return list
