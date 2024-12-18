def terminal_test(state):
    return isinstance(state, int)


def utility(state):
    return state


def successors(state):
    tree = {
        "root": ["A", "B"],
        "A": ["C", "D"],
        "B": ["E", "F"],
        "C": [3, 6],
        "D": [2, 3],
        "E": [7, 1],
        "F": [2, 0],
    }
    return tree.get(state, [])


def max_value(state, alpha, beta):
    if terminal_test(state):
        return utility(state)
    v = float("-inf")
    for s in successors(state):
        v = max(v, min_value(s, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def magic(state, alpha, beta):
    if terminal_test(state):
        return utility(state)
    v = float("-inf")
    for s in successors(state):
        v = max(v, magic(s, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(state, alpha, beta):
    if terminal_test(state):
        return utility(state)
    v = float("inf")
    for s in successors(state):
        v = min(v, max_value(s, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def pacman_game(c):
    tree = {
        "root": ["A", "B"],
        "A": ["C", "D"],
        "B": ["E", "F"],
        "C": [3, 6],
        "D": [2, 3],
        "E": [7, 1],
        "F": [2, 0],
    }

    root_value_no_magic = max_value("root", float("-inf"), float("inf"))
    print(root_value_no_magic)

    root_value_with_magic = magic("root", float("-inf"), float("inf"))

    if root_value_with_magic - c > root_value_no_magic:
        return root_value_with_magic - c, "Pac-Man should use dark magic"
    else:
        print(root_value_no_magic, root_value_with_magic)
        return root_value_no_magic, "Pac-Man should not use dark magic"


c = 3
result = pacman_game(c)
print(result)
