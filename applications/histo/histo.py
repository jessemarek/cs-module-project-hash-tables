# open the file
with open("robin.txt") as f:
    words = f.read()


# builds dict of words and their count
def word_count(s):
    # dictionary to store the word count
    d = {}

    # characters to ignore
    ignore = '":;,.-+=/\\|[]{}()*^&'

    # result of string after the ignored characters are removed
    r = ""

    # remove the ignored characters
    for c in s:
        if c not in ignore:
            r += c

    # take the string and split it into a list of words
    # removing any whitespace and forcing all characters
    # to lowercase
    words = r.strip().lower().split()

    # put each word into the dictionary and count it
    for i in range(len(words)):
        # check to see if the word already exists
        if words[i] not in d:
            # if not initialize it
            d[words[i]] = 0

        # increase the count of this word by 1
        d[words[i]] += 1

    return d


# create a histogram of the word count
def histogram(d):
    # dict of the words from the input file and their count
    words = word_count(d)

    # get the length of the longest word
    longest = len(max(words.keys(), key=lambda s: (len(s), s)))

    # sort the dict
    words = sorted(words.items(), key=lambda x: x[1], reverse=True)

    # print the word and the number of occurances represented by #s
    for word, count in words:
        # find spacing based off longest word in dict
        spacing = longest - len(word) + 4

        print(f"{word + ' ' * spacing + '#' * count}")


histogram(words)
