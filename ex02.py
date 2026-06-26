def descendentes(a):
    return [ nm for nm, _ in a[1] ] + \
           [ nm for f in a[1] for nm in descendentes(f) ]