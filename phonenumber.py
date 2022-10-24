"""_summary_
    Write a function that accepts an array of 10 integers (between 0 and 9), 
        that returns a string of those numbers in the form of a phone number.
    Example
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890" 
    The returned format must be correct in order to complete this challenge.
"""
def create_phone_number(n):
        #your code here\
    strnew = list(map(str,n))
    strlist = "".join(strnew)
    return "({}) {}-{}".format(strlist[:3],strlist[3:6],strlist[6:])

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])