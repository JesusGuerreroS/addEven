#################################################
#           Add only even numbers               #
#################################################
totalsum = 0
#calculate the total sum between even numbers
for n in range(2, 101, 2):
    totalsum += n

print(f"The total sum of even numbers from 1 to 100 is {totalsum}")