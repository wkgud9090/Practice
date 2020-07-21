import re
text = 'I saw a fox in the wood. The fox had red fur.'
pattern = re.compile(r'fox')
found = re.finditer(pattern, text)
for item in found:
    s = item.start()
    e = item.end()
    print(f'Found {text[s:e]} at {s}:{e}')