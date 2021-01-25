#!/usr/bin/env python3
import random


def average(numlist):
    """
    Find average of a list of numbers.

    Uses for loop to iterate through parameter NUMLIST
    and adds the sum of each element until the end of
    the list. AVERAGE then returns the sum divided by
    the length of NUMLIST.
    """
    numlist_sum = 0  # initialize sum to zero
    # Iterate over NUMLIST and add each element to the sum
    for num in numlist:
        numlist_sum += num

    # Return NUMLIST_SUM divided by LEN(NUMLIST) to calculate average
    return numlist_sum / len(numlist)


numlist = []  # Initialize empty NUMLIST
numlist_sum = 0  # Initialize zeroed NUMLIST_SUM.

# Append a random number between 0 and 100 to NUMLIST and add the number
# to NUMLIST_SUM.
for i in range(5):
    numlist.append(random.randint(0, 100))
    numlist_sum += numlist[i]

# Calculate average for later comparison.
numlist_average = numlist_sum / len(numlist)

# Print the (loop calculated) average
print("The average of numlist (for loop) is " + str(numlist_average))

# Compare NUMLIST_AVERAGE with 50 and display the results.
if numlist_average < 50:
    print("The average of numlist is less than 50")

elif numlist_average > 50:
    print("The average of numlist is greater than 50")

else:  # Otherwise, the average of NUMLIST == 50
    print("The average of numlist is equal to 50.")

# Output the value of NUMLIST.
print("The value of numlist is:")
print(numlist)

# Output the average of NUMLIST calculated with average().
print("The average of numlist (function) is " + str(average(numlist)))
