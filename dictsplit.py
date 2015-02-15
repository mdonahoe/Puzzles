"""
Split a string into a list of valid words
"""
import sys

words = file('/usr/share/dict/words').read().split('\n')
words = {word for word in words if len(word) > 1}
words.update(['i', 'a'])

def create_sentence(letters):
    if letters in words:
        return letters

    length = len(letters)
    if length < 1:
        return ''

    # Try to form the largest word we can from the front the of letters.
    while length > 0:
        sentence = create_sentence(letters[length:])
        if letters[:length] in words and sentence:
            return ''.join(letters[:length]) + ' ' + sentence
        length -= 1

    # We couldn't find anything here.
    return None

print create_sentence(sys.argv[1].lower())
