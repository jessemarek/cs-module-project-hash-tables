# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("ciphertext.txt") as f:
    text = f.read()


def crack_code(code):
    # frequency of letters in English in order of most to least occuring
    freq_letters = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')

    # dict to store the count of letters from input file
    count = {}

    # dict to store decode key
    key = {}

    # string to hold decoded message
    decoded_message = ""

    # characters to ignore
    ignore = ",.<>?;:'\"/\\|[]{}~!@#$%^&*()-+= \n”â€1234567890"

    # count occurrance of each character ignore special characters
    for c in code:
        if c not in ignore:
            # if the letter is not in the dict
            if c not in count:
                # add the letter and init the count to 0
                count[c] = 0

            # increment the count
            count[c] += 1

    # sort the dict by highest value first
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # build the decode dict
    for i in range(len(freq_letters)):
        key[count[i][0]] = freq_letters[i]

    # decode the text
    for c in code:
        # if character is in decode key
        if c in key:
            decoded_message += key[c]
        else:
            decoded_message += c

    print(decoded_message)


crack_code(text)
