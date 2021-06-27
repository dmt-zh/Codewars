# Given: an array containing hashes of names. Return: a string formatted as a list of names
# separated by commas except for the last two names, which should be separated by an ampersand.
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]) => returns 'Bart, Lisa & Maggie'

def namelist(names):
    if len(names) >= 1:
        l = [names[i]['name'] for i in range(0, len(names)-1)]
        return ', '.join(l) + ' & ' + names[-1]['name'] if len(names) > 1 else names[-1]['name']
    return ''

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))

