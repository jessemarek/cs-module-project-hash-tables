import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# create a list of all words from the input file
words = words.split()

# TODO: analyze which words can follow other words

# dict of words with a list of what words follow them
word_follows = {}

# list of words that can start a sentence
start_words = []

# dict of words that end a sentence
stop_words = {}

# build the dict of words that follow
for i in range(len(words)):
    # check if word exists in dict
    if words[i] not in word_follows:
        # if not init to an empty list
        word_follows[words[i]] = []

    # add the word following it to the list
    if i < len(words) - 1:
        word_follows[words[i]].append(words[i+1])

    # check if the word is a start word
    if words[i][0].isupper() or (words[i][0] == '"' and words[i][1].isupper()):
        # if word is a start word add it to the list
        start_words.append(words[i])

    # check to see if the word is a stop word
    if words[i][-1] in '.?!' or (words[i][-1] == '"' and words[i][-2] in '.?!'):
        # if word is a stop word add to dict
        if words[i] not in stop_words:
            stop_words[words[i]] = "stop"


# helper function that randomly selects a word from a list
def select_rand_word(words):
    rand_num = random.randint(0, len(words)-1)

    return words[rand_num]


# function to create a random sentence from the words
def sentence_maker():
    # keeps track of the current word. inits to a random start_word
    cur_word = select_rand_word(start_words)

    # init a string with the first word to hold our sentence as we build it
    s = f"{cur_word} "

    # keep building the sentence until we add a stop word
    while cur_word not in stop_words:
        cur_word = select_rand_word(word_follows[cur_word])
        s += f"{cur_word} "

    return s.strip()


# TODO: construct 5 random sentences
print(f"{sentence_maker()}\n")
print(f"{sentence_maker()}\n")
print(f"{sentence_maker()}\n")
print(f"{sentence_maker()}\n")
print(f"{sentence_maker()}\n")
