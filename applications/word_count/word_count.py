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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
