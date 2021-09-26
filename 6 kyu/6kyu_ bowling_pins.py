# Mount the Bowling Pins!
# Task:
# Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:
# I I I I  # each Pin has a Number:    7 8 9 10
#  I I I                                4 5 6
#   I I                                  2 3
#    I                                    1

# You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:
# I I   I
#  I   I
#   I
#    I

def bowling_pins(arr):
    import re
    bowls = '7 8 9 0\n 4 5 6 \n  2 3  \n   1   '
    for i in arr:
        if i == 10:
            i = str(0)
            bowls = re.sub(str(i), ' ', bowls)
        else:
            bowls = re.sub(str(i), ' ', bowls)
    return re.sub(r'\w', 'I', bowls)