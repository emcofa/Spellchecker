#!/usr/bin/python3

"""Throws errors"""

#kmom04 och 05
class Error(Exception):
    """User defined class for custom exceptions"""


class SearchMiss(Error):
    """Raised when misspelled word"""
