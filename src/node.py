"""
Node class
"""

class Node():
    """
    Node class
    """

    def __init__(self, letter):
        """
        Constructor
        """
        self.letter = letter
        self.is_end = False
        self.child = {}
