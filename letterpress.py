"""
A letterpress solver

What is the longest word we can spell using 25 letter tiles?

"""
import random
import string


import time
def timeonly(f):
    def g(*args, **kwds):
        t = time.time()
        f(*args, **kwds)
        return time.time() - t
    return g

def timeit(f):
    def g(*args, **kwds):
        t = time.time()
        ret = f(*args, **kwds)
        print '%s: %s' % (f.__name__, time.time() - t)
        return ret
    return g

#get some words
words = file('/usr/share/dict/words').read().split('\n')


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

def can_spell(word, letters):
    bag = make_bag(letters)
    for c in word:
        x = bag.get(c, 0)
        if x == 0:
            return False
        bag[c] = x - 1
    return True


def can_spell_bag(word, bag):
    removed = {}
    success = True
    for c in word:
        x = bag.get(c, 0)
        if x == 0:
            success = False
            break
        bag[c] = x - 1
        removed[c] = removed.get(c, 0) + 1

    for c,x in removed.iteritems():
        bag[c] += x
    return success

def can_spell_bag2(word, bag):
    removed = []
    success = True
    for c in word:
        x = bag.get(c)
        if not x:
            success = False
            break
        bag[c] = x - 1
        removed.append(c)

    for c in removed:
        bag[c] += 1 # no keyerrors expected
    return success

def search_(words, letters, func):
    longest = ''
    for word in words:
        if func(word, letters) and len(word) > len(longest):
            longest = word
    return longest

@timeit
def search2(words, letters):
    return search_(words, letters, can_spell)

@timeit
def search3(words, letters):
    return search_(words, letters, can_spell_list)

def can_spell_list(word, letters):
    bag = list(letters)
    for c in word:
        if c in bag:
            bag.remove(c)
        else:
            return False
    return True

@timeonly
def spell1(word, letters):
    return can_spell(word, letters)

@timeonly
def spell2(word, letters):
    return can_spell_list(word, letters)

@timeonly
def spell3(word, bag):
    return can_spell_bag(word, bag)

@timeonly
def spell4(word, bag):
    return can_spell_bag2(word, bag)

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



def test1():
    # generate a random letter set
    letters = [random.choice(string.lowercase) for _ in xrange(25)]
    print letters, len(words)
    print search(words, letters)
    print search2(words, letters)
    print search3(words, letters)
    print do_trie(words, letters)

def test2():
    # time different spelling functions
    letters = [random.choice(string.lowercase) for _ in xrange(10)]
    a = 0
    b = 0
    c = 0
    d = 0
    bag = make_bag(letters)
    print bag
    for word in words:
        a+=spell1(word, letters)
        b+=spell2(word, letters)
        c+=spell2(word, bag)
        d+=spell2(word, bag)
    print a,b,c,d
    print bag

test2()
