from math import log, sqrt
from numpy import subtract, array, sum as np_sum
from numpy.linalg import norm
from random import randint
from tkinter import Tk, Canvas, Button

CANVAS_W, CANVAS_H = 800, 600
NODE_R = 15
C1, C2, C3, C4 = 2, 50, 20000, 0.1


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, text):
        self.vec_force_sum = [0, 0]
        self.text = text
        self.targets = []
        self.vec = Vec(0, 0)

    def to(self, *nodes):
        for n in nodes:
            self.targets.append(n)
            n.targets.append(self)
        return self


class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, text):
        self.nodes.append(Node(text))
        return self.nodes[-1]


class GUI:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root, width=CANVAS_W, height=CANVAS_H, bg='ivory2')
        self.draw_button_1 = Button(root, text='Draw', command=self.draw)
        self.draw_button_2 = Button(root, text='Force redraw', command=self.force_redraw)
        self.canvas.pack()
        self.draw_button_1.pack()
        self.draw_button_2.pack()
        self.nodes = None
        self.busy = None

    def force_redraw(self):
        try:
            if self.busy:
                self.root.after_cancel(self.busy)
            for n in self.nodes:
                n.vec.x += n.vec_force_sum[0] * C4
                n.vec.y += n.vec_force_sum[1] * C4
            self.animate()
        except IndexError:
            return None

    def draw_node(self, x, y, text, r=NODE_R):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='violet red')
        self.canvas.create_text(x, y, text=text)

    def draw_graph(self):
        for n in self.nodes:
            for t in n.targets:
                self.canvas.create_line(n.vec.x, n.vec.y, t.vec.x, t.vec.y)
        for n in self.nodes:
            self.draw_node(n.vec.x, n.vec.y, n.text)

    def draw(self):
        if self.busy:
            self.root.after_cancel(self.busy)
        random_layout(self.nodes)
        self.animate()

    def animate(self):
        self.canvas.delete('all')
        force_layout(self.nodes)
        self.draw_graph()
        self.busy = self.root.after(50000, self.animate)


def random_layout(nodes):
    for n in nodes:
        n.vec.x = randint(NODE_R * 4, CANVAS_W - NODE_R * 4 - 1)
        n.vec.y = randint(NODE_R * 4, CANVAS_H - NODE_R * 4 - 1)


def force_layout(nodes):
    forces = {True: hooks_law, False: coulombs_law}
    for n in nodes:
        vec_force = array([forces[m in n.targets]([n.vec.x, n.vec.y], [m.vec.x, m.vec.y]) for m in nodes if n != m])
        for i in range(2):
            n.vec_force_sum[i] = float('{0:.4f}'.format(np_sum(vec_force[:, i])))


def unit(x):
    try:
        sq = sqrt(x[0] ** 2 + x[1] ** 2)
        if sq == 0:
            raise ZeroDivisionError
        return array([x[0] / sq, x[1] / sq])
    except ZeroDivisionError:
        return array([0, 0])


def hooks_law(u, v):
    try:
        return [float('{0:.4f}'.format(a)) for a in
                list(unit(subtract(v, u)) * C1 * log(norm(abs(subtract(u, v))) / C2))]
    except ValueError:
        return None


def coulombs_law(u, v):
    try:
        return [float('{0:.4f}'.format(a)) for a in
                list(unit(subtract(u, v)) * C3 / norm(abs(subtract(u, v))) ** 2)]
    except ValueError:
        return None


if __name__ == '__main__':
    graph = Graph()
    node = [graph.add(f'{x}') for x in range(1, 8)]
    node[0].to(*node[1:5])
    node[1].to(node[4])
    node[2].to(node[1], node[3])
    node[5].to(node[0], node[3], node[6])
    node[6].to(node[0], node[4])

    roots = Tk()
    w = GUI(roots)
    w.nodes = graph.nodes
    roots.mainloop()
