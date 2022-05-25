# basic Trie
import collections
from collections import Counter
'''# Given a bag of marbles with 8 red marbles,
# 4 blue marbles and 5 green marbles.
# Removing marbles one at a time from the bag,
# what is the likelihood of removing 4 marbles
# without removing a green marble? *'''

marbles = {'red': 8, 'blue': 4, 'green': 5}
# likelihood of removing 4 marbles without removing a green marble
# is the probability of removing 4 marbles from the bag
total = sum(marbles.values())
removing_red = marbles['red'] / total
removing_blue = marbles['blue'] / total
removing_green = marbles['green'] / total
removing_4_marbles_without_removing_green_marble = (
    removing_red + removing_blue)**4
# print(removing_4_marbles_without_removing_green_marble)

histogram = {"0": 10**5, "1": 10**2, "2": 10**1, "3": 10**0}
median = sum(histogram.values()) / 2
mean = sum(histogram.values()) / len(histogram)
mode = max(histogram, key=histogram.get)
# print("mean {} , median {} , mode {}".format(mean, median, mode))

#_____________________________________#

basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


# print('root -> {} \n'.format(basic_trie))
# print('root -> a -> d -> d ->{} \n'.format(basic_trie['a']['d']['d']))
# print('root -> a -> d -> {} \n'.format(basic_trie['a']['d']))
# print('root -> a ->  {} \n'.format(basic_trie['a']))
# print('root -> a -> d -> d -> word_end -> {} \n'.format(basic_trie['a']['d']['d']['word_end']))

#_____________________________________#
'''# You can lookup a word by checking if `word_end` is `True` after
# traversing all the characters in the word. Let's look at the word "hi".
# The first letter is "h", so you would call `basic_trie['h']`.
# The second letter is "i", so you would call `basic_trie['h']['i']`.
# Since there's no more letters left,
# you would see if this is a valid word by getting the value of `word_end`.
# Now you have `basic_trie['h']['i']['word_end']` with `True` or `False` if
# the word exists.

# In `basic_trie`, words "a" and "add" overlapp.
# This is where a Trie saves memory.
# Instead of having "a" and "add" in different cells,
# their characters treated like nodes in a tree.
# Let's see how we would check if a word exists in `basic_trie`.'''


def is_word(word):
    current_node = basic_trie
    for char in word:

        if char not in current_node:
            return False
        print('{} -> {}' .format(char, current_node[char]))
        current_node = current_node[char]

    return current_node['word_end']


# # Test words
# test_words = ['ap', 'add', 'adw', 'a', 'ad']
# for word in test_words:
#     if is_word(word):
#         print('"{}" is a word.'.format(word))
#     else:
#         print('"{}" is not a word.'.format(word))

#_____________________________________#

""" **Trie Using a Class**
-Just like most tree data structures,
# let's use classes to build the Trie.
# Implement two functions for the `Trie` class below.
# Implement `add` to add a word to the Trie.
# Implement `exists` to return `True` if the word exist in the
# trie and `False` if the word doesn't exist in the trie."""


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


# word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
# word_trie = Trie()

# # Add words
# for word in word_list:
#     word_trie.add(word)

# # Test words
# test_words = ['bear', 'goo', 'good', 'goos']
# for word in test_words:
#     if word_trie.exists(word):
#         print('"{}" is a word.'.format(word))
#     else:
#         print('"{}" is not a word.'.format(word))

#__________________________________________________#
'''
## Trie using Defaultdict (Optional)
This is an optional section.
Feel free to skip this and go to the next section of the classroom.

A cleaner way to build a trie is with a Python default dictionary.
The following `TrieNod` class is using `collections.defaultdict` instead
of a normal dictionary.
'''


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Tire(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):

        current_node = self.root
        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word
