
def how_many_steps(n_remaining, opts = range(1, 4, 1)):
    """A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. How many possible ways can the child run up 10 stairs?"""
    if n_remaining < 0: return 0
    elif n_remaining == 0: return 1
    else:
        solution = 0
        for opt in opts:
            solution = solution + how_many_steps(n_remaining - opt, opts = opts)
        return solution

how_many_steps(10, opts = (1, 2, 3))
