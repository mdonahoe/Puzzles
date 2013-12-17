"""
A letterpress cheater

What is the longest word we can spell using 25 letter tiles?

"""
import random
import string
import time

timings = {}
def track(f):
    def g(*args, **kwds):
        t = time.time()
        ret = f(*args, **kwds)
        v = time.time() - t
        k = f.__name__
        timings[k] = timings.get(k, 0) + v
        return ret
    return g

#get some words
words = file('/usr/share/dict/words').read().split('\n')

@track
def search_bag(words, bag):
    longest = ''
    for word in words:
        removed = []
        for c in word:
            if bag.get(c):
                removed.append(c)
                bag[c] -= 1
            else:
                break
        else:
            if len(word) > len(longest):
                longest = word

        for c in removed:
            bag[c] += 1

    return longest

def make_bag(letters):
    bag = {}
    for letter in letters:
        bag[letter] = bag.get(letter, 0) + 1
    return bag

def find_longest(trie, bag):
    longest = trie.get(_end, '')
    for i, letter in enumerate(bag):
        # are they words with this letter?
        subtrie = trie.get(letter)
        if not subtrie:
            continue

        # remove this letter
        bag[letter] -= 1
        if bag[letter] == 0:
            del bag[letter]

        # recursively get the longest word
        word = find_longest(subtrie, bag)
        if len(word) > len(longest):
            longest = word

        # add it back to the bag
        bag[letter] = bag.get(letter, 0) + 1

    # merge!
    return longest

_end = '@@'
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

@track
def trie_bag(trie, bag):
    return find_longest(trie, bag)

def test():
    # generate a random letter set
    T = make_trie(words)
    for _ in range(10):
        letters = [random.choice(string.lowercase) for _ in xrange(25)]
        bag = make_bag(letters)
        a = search_bag(words, bag)
        b = trie_bag(T, bag)
    print timings

test()

