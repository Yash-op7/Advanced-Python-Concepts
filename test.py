import this

# print(this.s)
linebreak = '-'*100
print(linebreak)
mappings = dict(this.d)
mappings[' '] = ' '
mappings[','] = ','
mappings['\n'] = '\n'
mappings['.'] = '.'
mappings['-'] = '-'
mappings["'"] = "'"
mappings['"'] = '"'
mappings['!'] = '!'
mappings['*'] = '*'


encoded_message = this.s

decoded_message = [mappings[char] if char != ' ' else ' ' for char in encoded_message]

print(''.join(decoded_message))