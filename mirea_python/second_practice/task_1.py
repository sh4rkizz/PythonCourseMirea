def f21(x):
    if x[3] == 'forth':
        return 12
    elif x[3] == 'kicad':
        if x[4] == 1975:
            return 9
        elif x[4] == 2006:
            return 10
        elif x[4] == 1974:
            return 11
    elif x[3] == 'muf':
        if x[2] == 'tea':
            return 8
        elif x[2] == 'alloy':
            if x[0] == 1985:
                return 6
            elif x[0] == 1983:
                return 7
        elif x[2] == 'mql4':
            if x[4] == 1974:
                if x[1] == 'tea':
                    return 4
                elif x[1] == 'krl':
                    return 5
            elif x[4] == 2006:
                if x[0] == 1985:
                    return 2
                elif x[0] == 1983:
                    return 3
            elif x[4] == 1975:
                if x[1] == 'tea':
                    return 0
                elif x[1] == 'krl':
                    return 1
