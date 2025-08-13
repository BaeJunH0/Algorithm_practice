def solution(m, n, puddles):
    # Initialize the grid with all zeros.
    # dp[i][j] will store the number of ways to reach (i, j).
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Mark puddles with -1. Adjusting coordinates from (1-based) to (0-based) for convenience.
    for r, c in puddles:
        dp[r][c] = -1

    # The starting point (1, 1) has 1 way to reach itself.
    dp[1][1] = 1

    # Iterate through the grid to fill the dp table
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            # If it's a puddle, skip it (already marked as -1)
            if dp[r][c] == -1:
                continue

            # If it's not the starting point (1, 1)
            if r == 1 and c == 1:
                continue

            # Calculate ways from above (if not a puddle)
            from_above = 0
            if r > 1 and dp[r - 1][c] != -1:
                from_above = dp[r - 1][c]

            # Calculate ways from left (if not a puddle)
            from_left = 0
            if c > 1 and dp[r][c - 1] != -1:
                from_left = dp[r][c - 1]

            # The total ways to reach (r, c) is the sum of ways from above and from left
            dp[r][c] = (from_above + from_left) % 1000000007

    # The answer is the number of ways to reach the school at (m, n)
    return dp[m][n]