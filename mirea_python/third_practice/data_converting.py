from struct import Struct, unpack_from, iter_unpack, calcsize


def f31(data):
    a = Struct(f'< H q 2I 4H h b q h')
    c = Struct('< 2I H I Q I f d')
    d = Struct('< h f d')

    un_a = a.unpack_from(data, data.index(b'FBIX') + 4)
    un_c = c.unpack_from(data, un_a[0])

    return {
        'A1': {
            'B1': {
                'C1': str(unpack_from(f'< {un_c[0]}s', data, offset=un_c[1])[0])[2:-1],
                'C2': list(unpack_from(f'< {un_c[2]}b', data, offset=un_c[3])),
                'C3': un_c[4],
                'C4': un_c[5],
                'C5': un_c[6],
                'C6': un_c[7]
            },
            'B2': un_a[1],
        },
        'A2': [{'D1': x[0], 'D2': x[1], 'D3': x[2]} for x in
               iter_unpack(d.format, data[un_a[3]:un_a[2] * d.size + un_a[3]])],
        'A3': [x[0] for x in iter_unpack('< f', data[un_a[5]: un_a[4] * calcsize('< f') + un_a[5]])],
        'A4': [x[0] for x in iter_unpack('< d', data[un_a[7]: un_a[6] * calcsize('< d') + un_a[7]])],
        'A5': un_a[8],
        'A6': un_a[9],
        'A7': un_a[10],
        'A8': un_a[11]
    }
