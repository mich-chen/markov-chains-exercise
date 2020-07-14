"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()
    # opens text file, reads text as string

# print(open_and_read_file("green-eggs.txt"))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    # print(words, '\n')

    # from 0 to len(words) - 2 to allow us to access index + 2
    for index in range(0, len(words) - 2):
        # set key as a tuple of bigrams
        key = (words[index], words[index + 1])
        if key not in chains:
            # check if key exists in dictionary
            # if not then create new key and set value to following word
            chains[key] = [words[index + 2]]
            
        else:
            # if key does exist in dictionary already
            # then append new following word into existing list of values
            chains[key].append(words[index + 2])
        
    return chains
       
    # for key, value in chains.items():
    #     print(key, ':', value)
    # print(chains)


def make_text(chains):
    """Return text from chains."""

    words = []

    
    bigram = random.choice(chains)
    following_word = random.choice(chains[bigram])
    link = bigram + following_word
    words.append(link)
    new_bigram = (bigram[1], random.choic(chain)[0])
    following_word = random.choice(chains[new_bigram])
    words.append(link)
    
    return " ".join(words)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
