# 1st month of coding
def factors(a_number):
    factors = [] # Create an array.

    for i in range(1, a_number + 1):
        # Go through all numbers below it
        if a_number % i == 0:
            # Does it divide into the number?
            factors.append(i)

    return factors

# 6th Months of Coding
def factors(x):
    f = []
    for i in range(1, x+1):
        if x % i == 0:
            f.append(i)


# Year of coding:
f = lambda x: [d for d in range(1,x+1) if x % i == 0]
