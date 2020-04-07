# Fill a 1-D array with random values, then print the values.
import random
import sys
import array
from arrays import Array

# The constructor is called to create the array.
value_list = Array(1)
print('size of array = ', sys.getsizeof(value_list))
compact_array = array.array('u',['a'])
print('size of compact array = ', sys.getsizeof(compact_array))
print('size of list = ',sys.getsizeof(['a']))

# Fill the array with random floating-point values.
for i in range(len(value_list)) :
    value_list[i] = random.random()
# Print the values, one per line.
for i in range(len(value_list)) :
    print(value_list[i])
for i in value_list:
    print(i)

# Count the number of occurrences of each letter in a text file.
# Create an array for the counters.
counters = Array(127)
counters.clear(0)
# Open the text file for reading and extract each letter.
f = open('textfile.txt', 'r')
letter = f.read(1)
while letter != "" :
    code = ord(letter)
    counters[code] = counters[code] + 1
    letter = f.read(1)
# Close the file
f.close()
# Print the results.
for i in range(26) :
    print( "{} - {:4d} {} - {:4d}".format(chr(65+i), counters[65+i],
                                      chr(97+i), counters[97+i]))

# get size of list
data = []
for i in range(15):
	a = len(data)
	b = sys.getsizeof(data)
	print(" Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
	data.append(None)
