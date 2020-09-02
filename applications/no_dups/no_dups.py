def no_dups(s):
    # dictionary to store words without duplicates
    d = {}

    # split the string into the separate words
    words = s.split()

    # go through the list of words and put them into a dict
    # this will prevent duplicate words from being stored
    for i in range(len(words)):
        if words[i] not in d:
            d[words[i]] = 0

    # join the words back together in order
    r = " ".join(d.keys()).strip()

    return r


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
