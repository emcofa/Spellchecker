#!/usr/bin/env python3

""" Module for testing the class Die """

import unittest
from src.trie import Trie
from src.exceptions import SearchMiss

# pylint: disable=protected-access


class TestSort(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def test_check_word_true(self):
        """ Test if word in Trie"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        check = h.check_word("transfusible")
        self.assertEqual(True, check)  # Assert

    def test_check_word_false(self):
        """ Test if error raises when word not in list"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)

        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.check_word("vattenmelon"))  # Assert

    def test_check_not_finished_word_false(self):
        """ Test if error raises when word not in the end"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)

        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.check_word("panopti"))  # Assert

    def test_search_prefix_true(self):
        """ Test if word in Trie"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        prefix = h.search_prefix("ala")
        self.assertEqual(['alarm', 'alarmed', 'alas', 'alabaster',
                         'aland', 'alanna', 'alamode', 'alagoas'], prefix)  # Assert
        prefix2 = h.search_prefix("alan")
        self.assertEqual(['aland', 'alanna'], prefix2)  # Assert
        prefix3 = h.search_prefix("aland")
        self.assertEqual(['aland'], prefix3)  # Assert

    def test_search_prefix_false(self):
        """ Test to write a prefix that doesn't exists and make sure not code crashes"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        prefix = h.search_prefix("qwe")
        self.assertEqual('', prefix)  # Assert

    def test_print_all_first(self):
        """ Test if correct word prints out"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        lista = h.print_all()
        self.assertEqual("aachen", lista[0])  # Assert
        self.assertEqual("zymotic", " ".join(lista[25401:]))  # Assert

    def test_print_all_type(self):
        """ Test if same type"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        lista = h.print_all()
        self.assertEqual(type("aachen"), type(lista[0]))  # Assert

    def test_delete_true(self):
        """Test to successfully delete word return"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        check = h.check_word("hallux")
        self.assertEqual(True, check)
        h.delete_node("hallux")
        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.check_word("hallux"))

    def test_delete_parts_of_many_words(self):
        """Test to delete a word that is a part of other words"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        check = h.check_word("zoom")
        self.assertEqual(True, check)
        h.delete_node("zoom")
        check2 = h.check_word("zoomorphic")
        check3 = h.check_word("zooming")
        self.assertEqual(True, check2)
        self.assertEqual(True, check3)
        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.check_word("zoom"))

    def test_delete_false(self):
        """Test to delete word that doesn't exists"""
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.delete_node("jordgubbe"))

    def test_delete_part_of_word(self):
        """Test to delete a part of a word and make sure the word not deletes """
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.delete_node("twadd"))
        check = h.check_word("twaddler")
        self.assertEqual(True, check)

    def test_delete_a_word_containing_a_word(self):
        """Test to delete a word that contains same word """
        h = Trie()
        with open("dictionary.txt", "r", encoding="utf-8") as fp:
            for word in fp:
                word = word.strip()
                h.add_word(word)
        h.delete_node("transformism")
        with self.assertRaises(SearchMiss):
            self.assertEqual(True, h.check_word("transformism"))
        check = h.check_word("transform")
        self.assertEqual(True, check)
