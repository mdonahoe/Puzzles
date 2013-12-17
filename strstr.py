import sys
a,b = sys.argv[1:]
def strstr(a,b):
    if not b: return True
    if not a: return False
    if a[0] == b[0] and strstr(a[1:], b[1:]):
        return True
    return strstr(a[1:], b)

if __name__ == '__main__':
    print strstr(a,b)
