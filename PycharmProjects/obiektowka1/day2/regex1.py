import re

def check_dice(text):
    regex = r'([1-9]\d*)?[dD](3|4|6|8|10|12|20)([+-]\d+)?'
    result  = re.search(regex, text)
    return bool(result)

print(check_dice('2D10+5'))

