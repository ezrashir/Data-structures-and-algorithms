# Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!



def stringifyNumbers(obj):
    newObj=obj
    for k,v in obj.items():
        if isinstance(v, dict):
            v = stringifyNumbers(v)
        if isinstance(v, int):
            newObj[k] = str(v)
    return newObj
