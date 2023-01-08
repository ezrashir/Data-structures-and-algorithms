# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.



def collectStrings(obj, list=[]):
    for k, v in obj.items():
        if isinstance(v, str):
            list.append(v)
        if isinstance(v, dict):
            list = collectStrings(v, list)
    return list
