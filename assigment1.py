# assignment1.py
import math

def find_period(L0: int, L1: int):
    """
    Prints the pendulum period for integer lengths from L0 to L1 inclusive (step 1 m).
    Returns the periods for L0 and L1 as (T0, T1).

    Uses g = 9.81 m/s^2 and T = 2 * pi * sqrt(L / g).
    Preconditions: L1 > L0 > 0 and both are integers.
    """
    if not (isinstance(L0, int) and isinstance(L1, int)):
        raise TypeError("L0 and L1 must be integers.")
    if not (L1 > L0 > 0):
        raise ValueError("Require L1 > L0 > 0 (both integers).")

    g = 9.81
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)

    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print(f"When L = {L:4.1f} m, T = {T:3.1f} s")

    return T0, T1

# Example usage
if __name__ == "__main__":
    find_period(2, 10)
