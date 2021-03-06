'''Typed wrappers for builtin Python functions.

This makes it easier to chain lots of things together in function composition
without having to manually add type signatures to Python builtins.

Each function is a `~hask3.lang.type_system.TypedFunc`:class: replacement of
the corresponding Python builtin with the right signature.

'''

from hask3.lang.syntax import H


def pycmp(a, b):
    '''Return negative if x<y, zero if x==y, positive if x>y.'''
    return 0 if a == b else (-1 if a < b else 1)


callable = callable ** (H/ "a" >> bool)
cmp = pycmp ** (H/ "a" >> "a" >> int)
delattr = delattr ** (H/ "a" >> str >> None)
divmod = divmod ** (H/ "a" >> "b" >> ("c", "c"))
getattr = getattr ** (H/ "a" >> str >> "b")
hasattr = hasattr ** (H/ "a" >> str >> bool)
hash = hash ** (H/ "a" >> int)
hex = hex ** (H/ int >> str)
isinstance = isinstance ** (H/ "a" >> "b" >> bool)
issubclass = issubclass ** (H/ "a" >> "b" >> bool)
len = len ** (H/ "a" >> int)
oct = oct ** (H/ int >> str)
repr = repr ** (H/ "a" >> str)
setattr = setattr ** (H/ "a" >> str >> "b" >> None)

# Sorted may take an optional key argument.  This cannot be properly capture
# by Hask.
sorted = sorted ** (H/ "a" >> list)

try:
    from __builtin__ import unichr as pyunichr
except ImportError:
    pyunichr = chr
    unicode = str

unichr = pyunichr ** (H/ int >> unicode)

del H
