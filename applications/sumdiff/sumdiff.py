"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# fn takes in a tuple of nums


def sum_diff(nums):
    # store all the sums in a dict
    sums = {}

    # store all the differnces in a dict
    diffs = {}

    # loop through tuple and add/subtract each combo of 2 numbers together
    for x in nums:
        for y in nums:
            # get the sum of the F(x)
            num_sum = f(x) + f(y)

            # store the result in sums dict along with
            # the numbers that gave the result
            if num_sum not in sums:
                # if entry not already in dict set it to an empty list
                sums[num_sum] = []
            # append the numbers to the list of possible numbers
            sums[num_sum].append((x, y))

            num_diff = None
            # get the difference of the F(x)
            if x > y:
                num_diff = f(x) - f(y)

            elif y > x:
                num_diff = f(y) - f(x)

            if num_diff not in diffs:
                # if entry not already in dict set it to an empty list
                diffs[num_diff] = []
            # append the numbers to the list of possible numbers
            diffs[num_diff].append((x, y))

    print(sums)
    print(diffs)


sum_diff(q)
