import re
string = open('inputstring.txt').read()
string = re.sub(r'(tre)\b', r'ter', string, flags=re.I|re.M)
string = re.sub(r'(tres)\b', r'ters', string, flags=re.I|re.M)
string = re.sub(r'(our)\b', r'or', string, flags=re.I|re.M)
string = re.sub(r'(ours)\b', r'ors', string, flags=re.I|re.M)
output = open('outputstring.txt', 'w')
output.write(string)