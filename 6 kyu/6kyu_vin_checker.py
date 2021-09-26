# In this Kata you should write a function to validate VINs, Vehicle Identification Numbers.
# Valid VINs are exactly 17 characters long, its composed of capital letters (except "I","O" and "Q") and digits.
# The 9th character is a MODULUS 11 check digit. Here is how it works:
# 1. Letters are converted to numbers
# Following the table bellow, letters are converted to numbers. "I","O" and "Q" are invalid characters.

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 1 2 3 4 5 6 7 8   1 2 3 4 5   7   9 2 3 4 5 6 7 8 9

# Ex.: VIN 5YJ3E1EA7HF000337 becomes 58135151786000337.

# 2. Each number is multiplied by a weight
# The weights are the following: [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2].

# VIN:     5   Y   J   3   E   1   E   A   7   H   F   0   0   0   3   3   7
# DECODED: 5   8   1   3   5   1   5   1   7   8   6   0   0   0   3   3   7
# WEIGHTS: 8   7   6   5   4   3   2   10  0   9   8   7   6   5   4   3   2
# PRODUCT: 40  56  6   15  20  3   10  10  0   72  48  0   0   0   12  9   14

# 3. All products are summed up
# Ex.: 40+56+6+15+20+3+10+10+0+72+48+0+0+0+12+9+14 = 315

# 4. The modulus 11 of the sum is taken
# Ex.: 315 mod 11 = 7

# 5. Check 9th character. If the 9th character matches the modulus 11, the VIN is valid.
# Ex.: 5YJ3E1EA7HF000337 is a valid VIN, 9th character is 7

# If the modulus 11 of the sum is equal to 10, then the digit is "X".
# Ex.: 5YJ3E1EAXHF000347 is a valid VIN.


def check_vin(vin_num):
    coder = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9, 'S': 2,
        'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9
    }
    decoded = []
    products = []
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    if len(vin_num) == 17:
        for s in vin_num:
            if s.isalpha():
                if s not in coder:
                    return False
                decoded.append(coder[s.upper()])
            else:
                decoded.append(int(s))
        for d, w in zip(decoded, weights):
            products.append(d * w)
        if sum(products) % 11 == 10 and vin_num[8] == 'X':
            return True
        elif str(sum(products) % 11) == str(vin_num[8]):
            return True
        else:
            return False
    return False


