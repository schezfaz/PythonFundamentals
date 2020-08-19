#Question:
# Rearrange the array such that elements at even positions are greater than all elements before it
# and elements at odd positions are less than all elements before it.
# Input : [1, 2, 3, 4, 5, 6, 7]
# Output : [4, 5, 3, 6, 2, 7, 1]

# 1. Get input array
# 2. sort array in ascending order
# 3. calculate length of the array
# 4. calculate no. of even and odd positions
# 6. initialise output array
# 6. get highest n  number of digits where n = no. of even positions
# 7. place result(6) at even positions in ascending order in output array
# 8. get lowest m number of digits where m = no. of odd positions
# 9. place result(7) at odd positions in descending order in output array

import math

input = [1,2,3,4,5,6,7]
print(input)
length = len(input)
if length%2!=0:
    even_pos = math.floor(length/2)
    odd_pos = length-even_pos
else:
    even_pos = odd_pos = int(length/2)

output = [None] * length
even_pos_digits = input[-even_pos:]
for i in range(0,even_pos):
    pos = (i*2)+1
    output[pos] = even_pos_digits[i]

odd_pos_digits = input[:odd_pos]
odd_pos_digits=odd_pos_digits[::-1]

for i in range(0,odd_pos):
    pos= i*2
    output[pos] = odd_pos_digits[i]

print(output)