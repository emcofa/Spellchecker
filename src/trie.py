"""Contains Trie class"""
from src.node import Node
from src.exceptions import SearchMiss


class Trie():
    """Trie class"""

    to_list = []
    all_words = []

    def __init__(self):
        self.root = Node("")

# Method to add word to Trie
    def add_word(self, word):
        """Adds word to Trie"""
        current = self.root
        for letter in word:
            if letter not in current.child:
                current.child[letter] = Node(letter)
            current = current.child[letter]
        current.is_end = True

# Method to check if word is in Trie or not
    def check_word(self, word):
        """Checks if word in Trie"""
        if word == "":
            raise SearchMiss
        current = self.root
        for letter in word:
            if letter not in current.child:
                raise SearchMiss
            current = current.child[letter]
        if current.is_end is False:
            raise SearchMiss
        return current.is_end

# Methods to search for prefix and print out words containing prefix
    def search_prefix(self, prefix):
        """Searching for prefix"""
        self.to_list = []
        current = self.root
        for letter in prefix:
            if letter in current.child:
                current = current.child[letter]
            else:
                return ""
        self.child_letters(current, prefix[:-1])
        return self.to_list

    def child_letters(self, current, prefix):
        """Traversal through child letters of prefix"""
        if current.is_end:
            self.to_list.append(prefix + current.letter)
        for child in current.child.values():
            self.child_letters(child, prefix + current.letter)


# Methods to print all the words in alphabetical order

    def print_all(self):
        """Print all words"""
        self.all_words = []
        list_word = []
        list_word = self.find_all()
        list_word.sort()
        return list_word

    def find_all(self):
        """Returns all words in a list"""
        keys_list = []
        for key in self.root.child:
            keys_list.append(key)
        for letter in keys_list:
            current = self.root
            current_letter = current.child[letter]
            self.find_child(current_letter)
        temp_list = []
        for words in self.all_words:
            temp_list.append(words.lower())
        return temp_list

    def find_child(self, current):
        """Find child of root"""
        for child in current.child.values():
            self.add_word_to_list(child, current.letter)

    def add_word_to_list(self, current, prefix):
        """Add words to list"""
        if current.is_end:
            self.all_words.append(prefix + current.letter)
        for child in current.child.values():
            self.add_word_to_list(child, prefix + current.letter)

# Metods to remove a word from Trie

    def delete_node(self, word):
        """returns deleted"""
        current = self.root
        counter = 0
        deleted = self.remove_node_trie(word, counter, current)
        return deleted

    def remove_node_trie(self, word, counter, current):
        """traversal method for delete"""
        if counter < len(word):
            letter = word[counter]
            if letter not in current.child:
                raise SearchMiss
        if counter == len(word):
            if current.is_end is False:
                raise SearchMiss
            current.is_end = False
            if len(current.child) == 0:
                return True
            return False
        current_child = current.child[letter]
        counter += 1
        node_to_delete = self.remove_node_trie(word, counter, current_child)
        if node_to_delete is True:
            del current.child[letter]
            if len(current.child) == 0:
                return True
        return False
