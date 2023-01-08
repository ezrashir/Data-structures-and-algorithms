# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.



def reverse(string):
    if len(string)==1:
        return string
    else:
        return string[-1]+reverse(string[:-1])

def isPalindrome(strng):
    if reverse(strng)==strng:
        return True
    else:
        return False
