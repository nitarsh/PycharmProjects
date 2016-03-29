neighbours_index = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]


def apply_rules(cell_state, live_neighbours_count):
    pass
    # return boolean


def find_live_neighbours(state, y, x):
    y_range = range(len(state))
    x_range = range(len(state[0]))
    possible_neighbours_index = map(lambda (_y, _x): (y + _y, x + _x), neighbours_index)
    effective_neighbours_index = filter(lambda (_y, _x): _y in y_range and _x in x_range, possible_neighbours_index)
    return sum(map(lambda (_y, _x): 1 if state(_y, _x) else 0, effective_neighbours_index))


def next_cell_state(state, x, y):
    return apply_rules(state[x][y], find_live_neighbours(state, x, y))


def next_state(state):
    columnLength = len(state)
    rowLength = len(state[0])
    for x in columnLength:
        for y in rowLength:
            yield next_cell_state(state, x, y)


x = 2
y = 2

print map(lambda (_y, _x): (y + _y, x + _x), neighbours_index)
