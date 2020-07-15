"""Generate Markov text from text files."""

import random
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()
    # opens text file, reads text as string

# print(open_and_read_file("green-eggs.txt"))


def make_chains(text_string, n):
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
    for index in range(0, len(words) - n):
        # set key as a tuple of bigrams
        key = []
        words_index = index
        for i in range(n):
            key.append(words[i + words_index])
        key = tuple(key)

        if key not in chains:
            # check if key exists in dictionary
            # if not then create new key and set value to following word
            chains[key] = [words[index + n]]
            
        else:
            # if key does exist in dictionary already
            # then append new following word into existing list of values
            chains[key].append(words[index + n])

       
    # for key, value in chains.items():
    #     print(key, ':', value)
    # print(chains)
    return chains



# ('Would', 'you', 'could', 'you') : ['in', 'with', 'in', 'with']
# ('you', 'could', 'you', 'in') : ['a', 'a']
# ('could', 'you', 'in', 'a') : ['house?', 'box?']
# ('you', 'in', 'a', 'house?') : ['Would']
# ('in', 'a', 'house?', 'Would') : ['you']
# ('a', 'house?', 'Would', 'you') : ['could']
# ('house?', 'Would', 'you', 'could') : ['you']
# ('you', 'could', 'you', 'with') : ['a', 'a']
# ('could', 'you', 'with', 'a') : ['mouse?', 'fox?']
# ('you', 'with', 'a', 'mouse?') : ['Would']
# ('with', 'a', 'mouse?', 'Would') : ['you']
# ('a', 'mouse?', 'Would', 'you') : ['could']
# ('mouse?', 'Would', 'you', 'could') : ['you']
# ('you', 'in', 'a', 'box?') : ['Would']
# ('in', 'a', 'box?', 'Would') : ['you']
# ('a', 'box?', 'Would', 'you') : ['could']
# ('box?', 'Would', 'you', 'could') : ['you']
# ('you', 'with', 'a', 'fox?') : ['Would']
# ('with', 'a', 'fox?', 'Would') : ['you']
# ('a', 'fox?', 'Would', 'you') : ['like']
# ('fox?', 'Would', 'you', 'like') : ['green']
# ('Would', 'you', 'like', 'green') : ['eggs']
# ('you', 'like', 'green', 'eggs') : ['and']
# ('like', 'green', 'eggs', 'and') : ['ham?']
# ('green', 'eggs', 'and', 'ham?') : ['Would']
# ('eggs', 'and', 'ham?', 'Would') : ['you']
# ('and', 'ham?', 'Would', 'you') : ['like']
# ('ham?', 'Would', 'you', 'like') : ['them,']
# ('Would', 'you', 'like', 'them,') : ['Sam']
# ('you', 'like', 'them,', 'Sam') : ['I']
# ('like', 'them,', 'Sam', 'I') : ['am?']


def make_text(chains):
    """Return text from chains."""
    
    words = []

    list_keys = list(chains.keys())
    # list of tuple keys
    key1 = random.choice(list_keys)
    value1 = random.choice(chains[key1])
    link1 = f'{" ".join(key1)} {value1}'
    words.append(link1)

    while key1 in chains:
        new_key = link1.split(" ")[1:]
        new_key_tuple = tuple(new_key)

        if new_key_tuple in chains.keys():
            new_value = random.choice(chains[new_key_tuple])
            words.append(new_value)
            key1 = new_key_tuple
            link1 = f'{" ".join(new_key_tuple)} {new_value}'
        else:
            break
    
    return " ".join(words)

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains)

print(random_text)
