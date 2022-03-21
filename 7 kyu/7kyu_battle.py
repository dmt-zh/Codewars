# Groups of characters decided to make a battle. Help them to figure out what group is more powerful.
# Create a function that will accept 2 variables and return the one who's stronger.

# Rules
# Each character has its own power:
#   A = 1, B = 2, ... Y = 25, Z = 26
#   a = 0.5, b = 1, ... y = 12.5, z = 13
# Only alphabetical characters can and will participate in a battle.
# Only two groups to a fight.
# Group whose total power (a + B + c + ...) is bigger wins.
# If the powers are equal, it's a tie.

# Examples
# "One", "Two"  -->  "Two"
# "ONE", "NEO"  -->  "Tie!"

def battle(x: str, y: str) -> str:
  x_sum = sum(ord(i) - 64 if i.isupper() else (ord(i) - 96) * 0.5 for i in x)
  y_sum = sum(ord(j) - 64 if j.isupper() else (ord(j) - 96) * 0.5 for j in y)
  return 'Tie!' if x_sum == y_sum else x if x_sum > y_sum else y

