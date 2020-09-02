"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# fn takes in a tuple of nums


def sum_diff(nums):
    # store all the sums in a dict
    sums = {}

    # store all the differnces in a dict
    diffs = {}

    # store the solutions to the problem
    solutions = {}

    # loop through tuple and add/subtract each combo of 2 numbers together
    for a in nums:
        for b in nums:
            # get the sum of the F(x)
            num_sum = f(a) + f(b)

            # store the result in sums dict along with
            # the numbers that gave the result
            if num_sum not in sums:
                # if entry not already in dict set it to an empty list
                sums[num_sum] = []
            # append the numbers to the list of possible numbers
            sums[num_sum].append((a, b))

            # get the difference of the F(x)
            num_diff = None

            if a > b:
                num_diff = f(a) - f(b)

                if num_diff not in diffs:
                    # if entry not already in dict set it to an empty list
                    diffs[num_diff] = []
                    # append the numbers to the list of possible numbers
                    diffs[num_diff].append((a, b))

            else:
                num_diff = f(b) - f(a)

                if num_diff not in diffs:
                    # if entry not already in dict set it to an empty list
                    diffs[num_diff] = []
                    # append the numbers to the list of possible numbers
                    diffs[num_diff].append((b, a))

            # check and see if the sum has a match in the diffs dict
            if num_sum in diffs:
                for c, d in diffs[num_sum]:
                    equation = (a, b, c, d)

                    if tuple(equation) not in solutions:
                        solutions[tuple(equation)] = [f(a), f(b), f(c), f(d)]

            # check and see if diff has a match in the sums dict
            if num_diff in sums:
                for c, d in sums[num_diff]:
                    if a > b:
                        equation = (c, d, a, b)

                        if tuple(equation) not in solutions:
                            solutions[tuple(equation)] = [
                                f(c), f(d), f(a), f(b)]

                    else:
                        equation = (c, d, b, a)

                        if tuple(equation) not in solutions:
                            solutions[tuple(equation)] = [
                                f(c), f(d), f(b), f(a)]

    for k, v in solutions.items():
        print(
            f"f({k[0]}) + f({k[1]}) = f({k[2]}) - f({k[3]})  {v[0]} + {v[1]} = {v[2]} - {v[3]}")


sum_diff(q)
