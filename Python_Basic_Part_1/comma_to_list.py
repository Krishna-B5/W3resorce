# Write a Python program which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

a = '3,5,7,23'
b = a.split(',') # ouput will be converted to list
print("Converted to list {0} ".format(b))
t1 = tuple(b)
print("converted to tuple {0} ".format(t1))