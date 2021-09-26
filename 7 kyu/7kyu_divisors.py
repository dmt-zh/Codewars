# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array
# with all of the integer's divisors(except for 1 and the number itself), from smallest to largest.
# If the number is prime return the string '(integer) is prime' (null in C#)
# (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
# divisors(12); should return [2,3,4,6]
def divisors(integer):
    j = []
    for i in range(2, len(range(integer)[::-1])):
        if integer % i == 0:
            j.append(i)
        else:
            pass
    if len(j) == 0:
        return (str(integer) + ' is prime')
    else:
        return j

print(divisors(3))