import random

"""                                                                         Problem 1                                                                           """


def is_end(d, m_d):
    return d == m_d


def children():
    return [-1, 1]


def max_v(s, a, b, d, m_d, winner):
    if is_end(d, m_d):
        return winner[s]
    v = float("-inf")
    for s in children():
        v = max(
            v,
            min_v(
                s * 2 + (1 if s == 1 else 0),
                a,
                b,
                d + 1,
                m_d,
                winner,
            ),
        )
        if v >= b:
            return v
        a = max(a, v)
    return v


def min_v(s, a, b, d, m_d, winner):
    if is_end(d, m_d):
        return winner[s]
    v = float("inf")
    for s in children():
        v = min(
            v,
            max_v(
                s * 2 + (1 if s == 1 else 0),
                a,
                b,
                d + 1,
                m_d,
                winner,
            ),
        )
        if v <= a:
            return v
        b = min(b, v)
    return v


def play_game(start_player):
    m_d = 5
    total_leaves = 2**m_d
    winner = [random.choice([-1, 1]) for _ in range(total_leaves)]

    points_scorpion = 0
    points_subzero = 0
    rounds_played = []

    for round_number in range(m_d):
        print(f"\nRound {round_number + 1} begins!")
        initial_s = 0

        if start_player == 0:
            winner_score = max_v(initial_s, float("-inf"), float("inf"), 0, m_d, winner)
        else:
            winner_score = min_v(initial_s, float("-inf"), float("inf"), 0, m_d, winner)

        round_winner = "Scorpion" if winner_score == -1 else "Sub-Zero"
        print(f"\nWinner of Round {round_number + 1}: {round_winner}")
        rounds_played.append(round_winner)

        if round_winner == "Scorpion":
            points_scorpion += 1
        else:
            points_subzero += 1

        if points_scorpion > m_d // 2:
            return "Scorpion", len(rounds_played), rounds_played
        if points_subzero > m_d // 2:
            return "Sub-Zero", len(rounds_played), rounds_played

        start_player = 1 - start_player

    who_won = "Scorpion" if points_scorpion > points_subzero else "Sub-Zero"
    return who_won, len(rounds_played), rounds_played


start_player = int(
    input("Enter the starting player (0 for Scorpion, 1 for Sub-Zero): ")
)

winner, total_rounds, round_winners = play_game(start_player)

print(f"\nGame Winner: {winner}")
print(f"Total Rounds Played: {total_rounds}")

"""                                                                         Problem 2                                                                           """


def is_end(s):
    return isinstance(s, int)


def utility(s):
    return s


def children(s):
    tree = {
        "root": ["A", "B"],
        "A": ["C", "D"],
        "B": ["E", "F"],
        "C": [3, 6],
        "D": [2, 3],
        "E": [7, 1],
        "F": [2, 0],
    }
    return tree.get(s, [])


def max_v(s, a, b):
    if is_end(s):
        return utility(s)
    v = float("-inf")
    for s in children(s):
        v = max(v, min_v(s, a, b))
        if v >= b:
            return v
        a = max(a, v)
    return v


def magic(s, a, b):
    if is_end(s):
        return utility(s)
    v = float("-inf")
    for s in children(s):
        v = max(v, magic(s, a, b))
        if v >= b:
            return v
        a = max(a, v)
    return v


def min_v(s, a, b):
    if is_end(s):
        return utility(s)
    v = float("inf")
    for s in children(s):
        v = min(v, max_v(s, a, b))
        if v <= a:
            return v
        b = min(b, v)
    return v


def play_game(c):
    tree = {
        "root": ["A", "B"],
        "A": ["C", "D"],
        "B": ["E", "F"],
        "C": [3, 6],
        "D": [2, 3],
        "E": [7, 1],
        "F": [2, 0],
    }

    root_value_no_magic = max_v("root", float("-inf"), float("inf"))

    root_value_with_magic = magic("root", float("-inf"), float("inf"))

    if root_value_with_magic - c > root_value_no_magic:
        return f"The new MinMax value is: {root_value_with_magic - c}. Pacman should use dark magic"
    else:
        return f"The new MinMax value is: {root_value_no_magic}. Pacman should not use dark magic"


c = int(input("Enter the value of c: "))
result = play_game(c)
print(result)
