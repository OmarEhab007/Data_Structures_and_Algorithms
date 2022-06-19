class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie: Check if char is in the dictionary keys
        if char not in self.children:
            self.children[char] = TrieNode()

    def find(self, char):
        # check if char is in this TrieNode
        if char in self.children:
            return True
        return False

    def __str__(self):
        # A description of this TrieNode
        trie_children = self.children
        count_children = len(trie_children)
        desc = ""
        for key, value in trie_children.items():
            if count_children > 1 or count_children == 0:
                desc += str(key) + "=>" + str(value) + "\n"
            else:
                desc += str(key) + "=>" + str(value)

        return desc

    def prefix_words(self, prefix):
        # Get all the complete words with a given prefix
        trie_children = self.children
        words = []
        if self.is_word:
            words.append(prefix)
        for key, value in trie_children.items():
            words.extend(value.prefix_words(prefix + key))
        return words

    def suffixes(self, suffix=''):
        # function that collects the suffix for
        # all complete words below this point
        prefixes_words = self.prefix_words(suffix)

        suffixes = []
        # discard the prefix and get the remaining characters
        for word in prefixes_words:
            suffixes.append(word[len(suffix):])

        return suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            # Add a child node in this Trie
            current_node.insert(char)
            # update the iterator to the next node
            current_node = current_node.children[char]
        # the last node
        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        # Return None if prefix is not found

        current_node = self.root

        if prefix == '' or prefix is None:
            return None

        for char in prefix:

            if not current_node.find(char):
                return None

            current_node = current_node.children[char]

        return current_node

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        if word == '' or word is None:
            return None

        for char in word:

            if not current_node.find(char):
                return False

            current_node = current_node.children[char]

        return current_node.is_word


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test words
test_words = [
    "ant", "anthology", "antagonist", "antonym", "anth",
    "fun", "function", "factory", "fu",
    "trie", "trigger", "trigonometry", "tripod", "tri"
]
print('Dictionary list: {}'.format(wordList))
print("\n\t Test Insert and exists functions\n")
for word in test_words:
    if MyTrie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))

print("\n\t Test find/prefix/suffix function\n")

test_prefixes = ['a', 'an', 'ant', 'anto', 'anth', '', None]
for prefix in test_prefixes:
    prefixNode = MyTrie.find(prefix)
    if prefixNode:
        print('"{}" is a prefix \n'.format(prefix))
        print('TrieNode: \n{}'.format(prefixNode.children.items()))
        print('Words with prefix "{}" : {} '.format(
            prefix, prefixNode.prefix_words(prefix)))
        print('Auto-complete:')
        print('\n'.join(prefixNode.suffixes()))
        print('\n')
    else:
        print('"{}" is not a prefix.\n {}\n'.format(prefix, prefixNode))
