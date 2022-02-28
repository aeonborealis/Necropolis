# Generating Random Numbers in Python
# Python Programming Techniques, basic functions and strategies. 

# Generating a Single Random Number 
# The random() method in random module generates a float number between 0 and 1

# Example 

import random 
n = random.random()
print(n)

# Output
# Running the above code gives us the following result - 

# 0.211220

# Generating Number in a Range 
# The randint() method generates an integer between a given range of numbers 

# Example 

import random 
n = random.randint(0,22)
print(n)

Output 
2 

# Generating a List of numbers Using for Loop
# We can use the above randint() method along with a for loop to generate a list of numbers. 
# We first create an empty list and then append the random numbers generated to the empty list one by one. 

# Example

import random 
randomlist = []
for i in range(0,5)
n = random.randint(1,30)
randomlist.append(n)
print(randomlist)

# Output
# Running the above code gives us the following result 

[10, 5, 21, 1, 17]

# Using random.sample()
# We can also use the sample() method available in random module to directly generate a list of random numbers
# Here we specify a range and give how many random numbers we need to generate 

# Example

import random
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(randge(10, 30), 5)
print(randomlist)

# Output 
# Running the above code gives us the following result 

[16, 19. 13, 18, 15]

