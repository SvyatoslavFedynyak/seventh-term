import re
import os
from functools import reduce

class _MaybeMonad(object):

    def __init__(self, just=None, nothing=False):
        self._just = just
        self._nothing = nothing

    def __rshift__(self, fn):
        if not self._nothing:
            res = fn(self._just)
            assert isinstance(res, _MaybeMonad), (
                "In Maybe context function result must be Maybe")
            self._just = res._just
            self._nothing = res._nothing
        return self

    @property
    def result(self):
        return (self._nothing, self._just)

nothing = lambda: _MaybeMonad(nothing=True)
just = lambda val: _MaybeMonad(just=val)
returnM = just

def gt6(password):
    if len(password) > 6:
        return just(password)
    return nothing()

def lt12(password):
    if len(password) < 12:
        return just(password)
    return nothing()

def lowcase(password):
    if re.search("[a-z]", password):
        return just(password)
    return nothing()

def upcase(password):
    if re.search("[A-Z]", password):
        return just(password)
    return nothing()

def spec(password):
    if re.search("[$#@]", password):
        return just(password)
    return nothing()

def pipeline(password):

    do = returnM(password) >> gt6 >> lt12 >> lowcase >> upcase >> spec
    return do.result[1]

def read_data():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'passwords.txt'), 'r') as file:
        return [x for x in file.read().split(",")]

print(list(filter(None.__ne__, list(map(pipeline, read_data())))))
