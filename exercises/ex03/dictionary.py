"""An exercise to work with unit tests and dictionaries"""

__author__: str = "730555924"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """A function that inverts the keys and values of a dictionary"""
    new_dict: dict[str, str] = {}
    for key in dictionary:  # accesses the key in the parameter
        if dictionary[key] in new_dict:
            raise KeyError("You messed up")  # tells you that value->key repeats
        new_dict[dictionary[key]] = (
            key  # switches values and keys and stores in a new dictionary
        )
    return new_dict


def count(number: list[str]) -> dict[str, int]:
    """A function that counts numbers in a list and converts to a dictionary"""
    dictionary: dict[str, int] = {}
    for key in number:
        if key in dictionary:
            dictionary[key] += 1  # says if value repeats, adds it to dictionary
        else:
            dictionary[key] = 1  # if value does is not already in dictionary, adds it
    return dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """A function that takes in a dictionary and spits out most popular value"""
    colors_list: list[str] = []
    for name in colors:
        colors_list.append(
            colors[name]
        )  # takes value from parameter and adds it to a list
    color_dict: dict[str, int] = count(
        colors_list
    )  # uses list as parameter for count function
    max_value: int = 0
    max_color: str = ""
    for rainbow in color_dict:  # rainbow is the key of color_dict
        if (
            color_dict[rainbow] > max_value
        ):  # values of color dict bigger than new variable
            max_value = color_dict[rainbow]
            max_color = rainbow
    return max_color


def bin_len(str_list: list[str]) -> dict[int, set[str]]:
    """A function that stores strs in a dictionary with a set"""
    new_dict: dict[int, set[str]] = {}
    for word in str_list:
        if len(word) not in new_dict:
            new_dict[len(word)] = {
                word
            }  # basically takes number of letters in word and adds it to new_dict
        else:
            new_dict[len(word)].add(
                word  # not encountered before, length of word and word added to new set
            )  # had not encountered .add in any class before a TA helped me.
    return new_dict


# huge s/o to the TAs of office hours: for every function here, I got their assistance
# thanks guys
