def f23(inp):
    date = []
    t = dict()
    tr = {'false': 'Нет', 'true': 'Да'}
    for i, j in inp:
        if i and j:
            t.update({i: j})
    inp = [[i, j] for i, j in t.items()]

    phone_numbers = [i.replace('-', '')[7:] for i, _ in inp]
    data = [j.split('#') for _, j in inp]
    truth = [tr.get(j) for _, j in data]
    
    for i, _ in data:
        i = list(reversed(i.split('.')))
        i[2] = i[2][2:]
        date.append('/'.join(i))

    return [phone_numbers, truth, date]
