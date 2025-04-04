"""The unit test portion of dictionary.py"""

__author__: str = "730555924"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len

invert({"r": "f", "p": "b", "c": "i", "g": "s"})  # use case example
invert({"r": "f", "p": "z", "c": "i", "g": "l"})  # use case example
invert({"r": "f", "p": "f", "c": "i", "g": "s"})  # edge case example (2 values repeat)

count(["true", "false", "true", "true"])  # use case example
count(["flower", "bee", "tree", "bee", "meadow"])  # use case example
count(
    ["Edge", "edge", "case"]
)  # edge case example (2 of the same word but different spellings repeat)

favorite_color({"taylor": "yellow", "ben": "blue"})  # use case example
favorite_color({"julia": "red", "ben": "red", "taylor": "red"})  # use case example
favorite_color(
    {"taylor": "blue", "ben": "blue", "sam": "red", "tilly": "red"}
)  # edge case example (values of same # times repeated occur)

bin_len(["live", "laugh", "love"])  # use case example
bin_len(["true", "false", "kinda true"])  # use case example
bin_len([])  # edge case example (empty list)
