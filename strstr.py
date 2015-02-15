def strstr(haystack, needle):
    "Find the needle's location in the haystack, if it exists."
    if not needle:
        return 0

    if not haystack:
        return -1

    if haystack[0] == needle[0] and strstr(haystack[1:], needle[1:]) == 0:
        return 0

    # Advance 1 letter in the haystack.
    index = strstr(haystack[1:], needle)

    # Adjust the index if it was found.
    return index + 1 if index != -1 else -1


if __name__ == '__main__':
    import sys
    a, b = sys.argv[1:]
    print strstr(a, b)
