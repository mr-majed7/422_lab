import random


def terminal_test(depth, max_depth):
    """Checks if we have reached the leaf nodes."""
    return depth == max_depth


def successors(state):
    """Generates successor states."""
    return [-1, 1]


def max_value(state, alpha, beta, depth, max_depth, outcomes):
    if terminal_test(depth, max_depth):
        return outcomes[state]
    v = float("-inf")
    for s in successors(state):
        v = max(
            v,
            min_value(
                state * 2 + (1 if s == 1 else 0),
                alpha,
                beta,
                depth + 1,
                max_depth,
                outcomes,
            ),
        )
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(state, alpha, beta, depth, max_depth, outcomes):
    if terminal_test(depth, max_depth):
        return outcomes[state]
    v = float("inf")
    for s in successors(state):
        v = min(
            v,
            max_value(
                state * 2 + (1 if s == 1 else 0),
                alpha,
                beta,
                depth + 1,
                max_depth,
                outcomes,
            ),
        )
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def mortal_kombat_simulation(start_player):
    """Simulates the Mortal Kombat game."""
    max_depth = 5
    total_leaves = 2**max_depth
    outcomes = [random.choice([-1, 1]) for _ in range(total_leaves)]
    print("Utility values of leaf nodes:", outcomes)

    scorpion_wins = 0
    subzero_wins = 0
    rounds_played = []

    for round_number in range(max_depth):
        print(f"\nRound {round_number + 1} begins!")
        initial_state = 0  # Root state

        if start_player == 0:
            winner_score = max_value(
                initial_state, float("-inf"), float("inf"), 0, max_depth, outcomes
            )
        else:
            winner_score = min_value(
                initial_state, float("-inf"), float("inf"), 0, max_depth, outcomes
            )

        round_winner = "Scorpion" if winner_score == -1 else "Sub-Zero"
        rounds_played.append(round_winner)

        if round_winner == "Scorpion":
            scorpion_wins += 1
        else:
            subzero_wins += 1

        # Early termination if one player has already won the majority
        if scorpion_wins > max_depth // 2:
            return "Scorpion", len(rounds_played), rounds_played
        if subzero_wins > max_depth // 2:
            return "Sub-Zero", len(rounds_played), rounds_played

        # Alternate starting player for the next round
        start_player = 1 - start_player

    # Determine the overall winner after all rounds
    game_winner = "Scorpion" if scorpion_wins > subzero_wins else "Sub-Zero"
    return game_winner, len(rounds_played), rounds_played


# Input: starting player (0 for Scorpion, 1 for Sub-Zero)
start_player = int(
    input("Enter the starting player (0 for Scorpion, 1 for Sub-Zero): ")
)

# Run the simulation
winner, total_rounds, round_winners = mortal_kombat_simulation(start_player)

# Output the results
print(f"\nGame Winner: {winner}")
print(f"Total Rounds Played: {total_rounds}")
for i, round_winner in enumerate(round_winners, 1):
    print(f"Winner of Round {i}: {round_winner}")
