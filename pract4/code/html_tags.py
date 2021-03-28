from contextlib import contextmanager


class HTML:
    @contextmanager
    def body(self):
        print('<body>')
        yield
        print('</body>')

    @contextmanager
    def div(self):
        print('<div>')
        yield
        print('</div>')

    @staticmethod
    def p(line):
        print(f'<p>{line}</p>')


if __name__ == '__main__':
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
