from .damerau_levenshtein import *
from .levenshtein import *
from .block_distance import *

_method = Levenshtein()

def use(mode='ED', verbose=False):
    global _method
    if mode == 'ED':
        if verbose:
            print('mode change to Levenshtein')
        _method = Levenshtein()
    elif mode == 'DL':
        if verbose:
            print('mode change to DamerauLevenshtein')
        _method = DamerauLevenshtein()
    elif mode == 'BD':
        if verbose:
            print('mode change to BlockDistance')
        _method = BlockDistance()
    else:
        raise NotImplementedError

def similarity(s, t):
    global _method
    return _method.similarity(s, t)

def dissimilarity(s, t):
    global _method
    return _method.dissimilarity(s, t)

def distance(s, t):
    global _method
    return _method.distance(s, t)