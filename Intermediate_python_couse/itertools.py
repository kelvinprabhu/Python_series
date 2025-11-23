"""itertools examples and short notes.

This module demonstrates commonly-used functions from the built-in `itertools`
module and documents their purpose with short, runnable examples. The examples
are organized into demo functions and guarded by a `__main__` check so the file
can be imported without running demonstrations.

Category highlights:
- Infinite iterators: `count()`, `cycle()`, `repeat()`
- Finite iterators / filtering: `chain()`, `compress()`, `dropwhile()`, `groupby()`, `accumulate()`
- Combinatoric iterators: `product()`, `permutations()`, `combinations()`, `combinations_with_replacement()`

Run the file as a script to see example output:

    python3 Intermediate_python_couse/itertools.py

"""

from itertools import (
    count,
    cycle,
    repeat,
    chain,
    compress,
    dropwhile,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    groupby,
    accumulate,
)


def demo_infinite_iterators():
    """Demonstrate `count`, `cycle`, and `repeat`.

    These iterators are potentially infinite; the demo stops them explicitly
    to avoid endless loops.
    """
    print("\n--- Infinite iterators demo ---")
    # count: infinite sequence of integers starting at 10
    for i in count(10):
        if i == 13:  # stop early for demo purposes
            print("count stopped at", i)
            break

    # cycle: repeat an iterable over and over
    print("cycle output:", end=" ")
    c = 0
    for ch in cycle("ABC"):
        print(ch, end=" ")
        c += 1
        if c == 6:
            print("(stopped)")
            break

    # repeat: repeat a single value N times
    print("repeat output:")
    for item in repeat("X", 3):
        print(item)


def demo_finite_iterators():
    """Demonstrate finite iterator helpers: chain, compress, dropwhile, groupby, accumulate."""
    print("\n--- Finite iterators / filtering demo ---")

    # chain: combine multiple iterables into one sequence
    print("chain example:", "".join(chain("ABC", "DEF")))

    # compress: select elements where the selectors are truthy
    data = range(10)
    selectors = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
    print("compress example:", list(compress(data, selectors)))

    # dropwhile: drop elements while predicate is true, then yield the rest
    data2 = [1, 2, 3, 4, 5, 6, 7]
    print("dropwhile example:", list(dropwhile(lambda x: x < 4, data2)))

    # groupby: group *consecutive* items by a key function
    print("groupby example:")
    for key, grp in groupby("AAAABBBCCDAA"):
        print(key, list(grp))

    # accumulate: running totals (or other binary functions)
    print("accumulate example:", list(accumulate([1, 2, 3, 4])))


def demo_combinatoric_iterators():
    """Show combinatoric functions. Results are finite but can be large."""
    print("\n--- Combinatoric iterators demo ---")

    print("product example:", list(product("AB", "12")))

    # permutations: number of outputs is factorial in length of input
    print("permutations example (small input):", list(permutations("ABC")))

    print("combinations example:", list(combinations("ABCD", 2)))

    print(
        "combinations_with_replacement example:",
        list(combinations_with_replacement("AB", 2)),
    )


if __name__ == "__main__":
    demo_infinite_iterators()
    demo_finite_iterators()
    demo_combinatoric_iterators()