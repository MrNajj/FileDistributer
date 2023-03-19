import os

import easygui

# Temporary input creator that helps with the first backSlash
path_creator = "/" + input("create your path, to accses your downloads folder. {case sensistve}")


def file_lister(path):
    """
    This function lists all the files (none_directory files) in a given path of such directory or file
    :param path:  A proper spelled and capitalized path without the starting backSlash
    :return: A list of non Directory files in the given directory
    """
    downloads_counter = []
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            downloads_counter.append(entry)
    return downloads_counter


# Still testing the message Box (brainStorming new Ideas with this GUI) and how to implement.
choice_list = ["Downloads", "Documents"]
inp = ''
# To evalueate the input of the Box give it a varabiable to work with it.
while inp is not None:
    inp = easygui.buttonbox("Where do you want your file to go", "File Distribute", choice_list)
    if inp == "Downloads":
        print("Downloads")
        inp = None
    if inp == "Documents":
        print("Documents")
        inp = None
    elif inp == "off":
        print("None")
        inp = None
