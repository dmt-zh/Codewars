# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
# human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    import time
    if seconds <= 86399:
        return time.strftime("%H:%M:%S", time.gmtime(seconds))
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        if len(str(minutes)) < 2:
            minutes = '0' + str(minutes)
        if len(str(seconds)) < 2:
            seconds = '0' + str(seconds)
            return '{}:{}:{}'.format(hours, minutes, seconds)
        return '{}:{}:{}'.format(hours, minutes, seconds)