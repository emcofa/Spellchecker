#!/usr/bin/python3
""" Main file with Handler class """
# pylint: skip-file
import sys
import inspect
from src.exceptions import SearchMiss
from src.trie import Trie


class SpellChecker:
    """ Handler class """

    _OPTIONS = {
        "1": "check_word",
        "2": "search_prefix",
        "3": "change_file",
        "4": "print_all",
        "5": "remove_node",
        "6": "quit"
    }

    def __init__(self):
        """ Initialize class """
        self.trie = Trie()

    def read_file(self, filename="dictionary.txt"):
        """
        Read filename
        """
        self.trie = Trie()
        with open(filename, "r") as fp:
            for word in fp:
                word = word.strip()
                self.trie.add_word(word)

    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self._OPTIONS[method_name])

    def _print_menu(self):
        """
        Use docstring from methods to print options for the program.
        """
        menu = ""

        for key in self._OPTIONS:
            method = self._get_method(key)
            docstring = inspect.getdoc(method)

            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu)

    def check_word(self):
        """ Check if word is spelled correctly """
        word = input("\nEnter a word: \n>>> ").lower()
        try:
            self.trie.check_word(word)
            print(f"The word '{word}' was spelled correctly")
        except SearchMiss:
            print(f"word does not exist")

    def search_prefix(self):
        """ Search for prefix """
        counter = 0
        prefix = input("\nEnter a prefix (minimum 3 letters): \n>>> ").lower()
        if len(prefix) < 3:
            print("You have to enter minimum 3 letters!")
        else:
            words = self.trie.search_prefix(prefix)
            for word in words:
                print(word)
                counter += 1
                if counter == 10:
                    break
            prefix2 = ""
            while prefix2 != "quit":
                if prefix2 == "quit":
                    return
                else:
                    prefix2 = input(
                        f"Enter another letter, 'quit' to stop: {prefix}")
                    counter = 0
                    concat = prefix + prefix2
                    prefix = prefix + prefix2
                    words2 = self.trie.search_prefix(concat)
                    for word in words2:
                        print(word)
                        counter += 1
                        if counter == 10:
                            break

    def change_file(self):
        """Change file"""
        files = ["dictionary.txt", "frequency.txt",
                 "tiny_dictionary.txt", "tiny_frequency.txt"]
        inp = input("Enter filename: ")
        if inp not in files:
            print(f"Filename doesn't exists.\n")
        else:
            self.read_file(inp)
            print(f"Filename changed.\nCurrent filename: {inp}")

    def print_all(self):
        """ Print all words in trie """
        words = self.trie.print_all()
        for word in words:
            print(word)

    def remove_node(self):
        """Remove word from trie"""
        word = input("Enter a word to remove from trie: ").lower()
        try:
            self.trie.delete_node(word)
            print(f"The word '{word}' was removed from trie")
        except SearchMiss:
            print(f"word is missing")

    @staticmethod
    def quit():
        """ Quit the program """
        sys.exit()

    def main(self):
        """ Start method """
        self.read_file()
        while True:
            self._print_menu()
            choice = input("Enter menu selection:\n-> ")

            try:
                self._get_method(choice.lower())()
            except KeyError:
                print("Invalid choice!")
            input("\nPress enter to continue...")


if __name__ == "__main__":
    h = SpellChecker()
    h.main()
