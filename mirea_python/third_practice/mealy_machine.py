class C32:
    def __init__(self):
        self.current_state = 'A'
        self.states = {
            'A': {'look': ('B', 0), 'peek': ('A', 1)},
            'B': {'look': ('C', 2)},
            'C': {'move': ('A', 4), 'peek': ('C', 5), 'look': ('D', 3)},
            'D': {'look': ('E', 6), 'peek': ('F', 7)},
            'E': {'look': ('F', 8)},
            'F': {}
        }

    def move_method(self, method):
        try:
            state_worker = self.states.get(self.current_state).get(method)
            if state_worker is None:
                raise RuntimeError
            self.current_state = state_worker[0]
            return state_worker[1]
        except RuntimeError:
            return None

    def look(self):
        return self.move_method('look')

    def move(self):
        return self.move_method('move')

    def peek(self):
        return self.move_method('peek')
