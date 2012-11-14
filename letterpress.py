"""
A letterpress solver

What is the longest word we can spell using 25 letter tiles?

"""
import random
import string


import time
def timeit(f):
    def g(*args, **kwds):
        t = time.time()
        ret = f(*args, **kwds)
        print '%s: %s' % (f.__name__, time.time() - t)
        return ret
    return g

#get some words
words = file('/usr/share/dict/words').read().split('\n')

# generate a random letter set
letters = [random.choice(string.lowercase) for _ in xrange(25)]

@timeit
def search(words, letters):
    """for every word, see if we can spell it.
    keep track of the longest

    dependencies:
    number of characters in the dictionary
    * num letters (though this can be optimized)
    """
    longest = ''
    for word in words:
        bag = list(letters)
        for c in word:
            if c in bag:
                bag.remove(c)
            else:
                break
        else:
            if len(word) > len(longest):
                longest = word
    return longest

@timeit
def do_trie(words, letters):
    """build a trie, then recursively look for the longest word"""
    t = time.time()
    T = make_trie(words, limit=len(letters))
    B = make_bag(letters)
    return find_longest(T,B)

def make_bag(letters):
    bag = {}
    for letter in letters:
        bag[letter] = bag.get(letter, 0) + 1
    return bag

def find_longest(subtrie, bag):
    if not subtrie:
        return ''

    longest = subtrie.get(_end, '')
    for i, letter in enumerate(bag):
        # remove this letter
        bag[letter] -= 1

        # remove the key for less iteration
        if bag[letter] == 0:
            del bag[letter]

        # recursively get the longest word
        word = find_longest(subtrie.get(letter), bag)
        if len(word) > len(longest):
            longest = word

        # add it back to the bag
        bag[letter] = bag.get(letter, 0) + 1

    # merge!
    return longest

_end = '@@'

@timeit
def make_trie(words, limit=None):
    root = dict()
    for word in words:
        current_dict = root
        for i,letter in enumerate(word):
            if limit and i == limit: break
            current_dict = current_dict.setdefault(letter, {})
        else:
            current_dict = current_dict.setdefault(_end, word)
    return root



print letters, len(words)
print search(words, letters)
print do_trie(words, letters)
