# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

now = datetime.datetime.now()
now1 = str(now)
print("------------------------")
print(now1[0:19])
print("------------------------")