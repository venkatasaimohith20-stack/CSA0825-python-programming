from functools import lru_cache
import sys
calls_naive = 0
def ways_naive(n):
    """Ways to climb n temple steps taking 1 or 2 steps at a time (naive)."""
    global calls_naive
    calls_naive += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)
calls_memo = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    """Ways to climb n temple steps using memoisation."""
    global calls_memo
    calls_memo += 1
    # TODO 1 Solution:
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)
def ways_iterative(n):
    """Iterative approach using O(1) space keeping only the last two values."""
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return current
print("--- Q6 Outputs ---")
print(f"Naive for n=25 -> Ways: {ways_naive(25)}, Calls: {calls_naive}")
print(f"Memo  for n=25 -> Ways: {ways_memo(25)}, Calls: {calls_memo}")
try:
    # ways_memo(1000) would hit Python's default recursion limit (~1000)
    print(f"Current Recursion Limit: {sys.getrecursionlimit()}")
    # To safely compute large inputs without raising RecursionError:
    print(f"Iterative for n=1000 -> Ways (last 10 digits): {str(ways_iterative(1000))[-10:]}")
except Exception as e:
    print("Error encountered:", e)