def unique(inp):
    t = dict()
    for i, j in inp:
        if i and j:
            t.update({i: j})
    inp = [[i, j] for i, j in t.items()]
    return inp
