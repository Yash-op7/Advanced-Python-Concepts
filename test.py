s = 'zbax'

converted_string = ''.join([str(ord(c) - ord('a') + 1) for c in s])
print(converted_string)