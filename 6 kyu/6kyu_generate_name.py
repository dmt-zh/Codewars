# Create a function for generating a random 6 character string which will be used to access the photo URL.
# To make sure the name is not already in use, you are given access to an PhotoManager object.
# You can call it like so to make sure the name is unique:
# - photoManager.nameExists('ABCDEF'); // returns true
# - photoManager.nameExists('BBCDEF'); // returns false
# Note: We consider two names with same letters but different cases to be unique.

import string
import random

def generateName(length=6):
    name = ''.join((random.choice(string.ascii_letters) for _ in range(length)))
    while photoManager.nameExists(name):
        continue
    else:
        return name