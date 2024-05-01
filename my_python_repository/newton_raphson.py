""" Newton-Raphson method and associated functions"""

from typing import Callable
import math
import numpy as np
import matplotlib.pyplot as plt


def target_function(x: float) -> float:
    """Target function to find/estimate the roots"""
    return -math.log10(x) / x


def prime_of_target(x: float) -> float:
    """Prime of the target function"""
    return (math.log10(x) - 1) / x**2


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x_n: float,
    tol: float = 1e-8,
) -> float:
    """Uses the Newton-Raphson method to find/estimate the roots of a function.
    
    Args:
        f : Target function to find/estimate the root.
        df : Prime of the target function.
        x_n : Initial guess.
        tol : Error tolerance for the approximation.

    Returns:
        The value of the root.
    """
    x_n_plus_one = x_n - f(x_n) / df(x_n)
    while abs(x_n_plus_one - x_n) > tol:
        x_n = x_n_plus_one
        x_n_plus_one = x_n - f(x_n) / df(x_n)
    return x_n_plus_one


def __test_newton_raphson() -> None:
    """Plots the target function, its prime and the root"""
    x = np.linspace(0.1, 2, 200)
    root = newton_raphson(target_function, prime_of_target, 0.01)
    target = [target_function(item) for item in x]
    prime = [prime_of_target(item) for item in x]
    plt.axis((0.1, 2, -4, 4))
    plt.axhline(y=0, c='black', lw=0.5, linestyle='-')
    plt.plot(x, target, c="red", label=f"f(x) actual root: {1:.3f}")
    plt.plot(x, prime, c="blue", label="f\u2032(x)")
    plt.plot(root, 0, c="black", linestyle="", marker="o", label=f"Newton-Raphson estimate: {root:.9f}")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    __test_newton_raphson()