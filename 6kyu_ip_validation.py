# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89

# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

# Notes: Leading zeros (e.g. 01.02.03.04) are considered invalid

def is_valid_IP(ipv):
    import re
    valid = re.match('^\d{,3}.\\d{,3}.\\d{,3}.\\d{,3}$', ipv)
    if valid:
        if any(re.match('0[1-9]\d{,2}', i) for i in valid.group().split('.')):
            return False
        elif len(valid.group().split('.')) <= 3:
            return False
        elif any(255 < int(i) for i in valid.group().split('.')):
            return False
        else:
            return True
    return False