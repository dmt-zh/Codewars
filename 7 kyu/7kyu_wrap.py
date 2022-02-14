# It's your best friend's birthday! You already bought a box for the present.
# Now you want to pack the present in the box. You want to decorate the box with a ribbon and a bow.

# But how much cm of ribbon do you need?
# Write the method wrap that calculates that!
# A box has a height, a width and a length (in cm). The ribbon is crossed on the side with the largest area.
# Opposite this side (also the side with the largest area) the loop is bound, calculate with 20 cm more tape.

# Examples:
# wrap(17,32,11) => 162
# wrap(13,13,13) => 124
# wrap(1,3,1) => 32

def wrap(height, width, length):
    sides = sorted([height, width, length])
    return 20 + sides[0] * 4 + (sides[1] + sides[2]) * 2