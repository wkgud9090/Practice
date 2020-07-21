import re
words = ('book', 'bookworm', 'Bible',
    'bookish','cookbook', 'bookstore', 'pocketbook')
pattern = re.compile(r'^book$')
for word in words:
    if re.search(pattern, word):
        print(f'The {word} matches')