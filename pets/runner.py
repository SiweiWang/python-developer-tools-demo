"""

runner.py
~~~~~~~~~

This module provides a simple pets classes (Cats and Dogs). You can use it like this:

    >>> from pets.runner import run
    >>> run()
    Meow
    Wolf
    >>> from pets.cat import Cat
    >>> c = Cat()
    >>> c.sound()
    Meow
"""

__author__ = 'Siwei Wang'

from pets.cat import Cat
from pets.dog import Dog

def run():
    c = Cat()
    c.sound()
    d = Dog()
    d.sound()

