# itertools module in Python provides a collection of tools for handling iterators.
# It is a standard library module that offers various functions that work on iterators to produce complex
# iterators. These functions are useful for creating efficient and memory-friendly code, especially when dealing
# with large datasets or infinite sequences. The itertools module includes functions for: 
# 1. Infinite iterators: count(), cycle(), repeat()
# 2. Finite iterators: chain(), compress(), dropwhile(), filterfalse(),
#    groupby(), islice(), starmap(), takewhile(), tee(), zip_longest()
# 3. Combinatoric iterators: product(), permutations(), combinations(), combinations_with_replacement()
import itertools
# count - used to generate an infinite sequence of numbers, starting from a specified value and incrementing by a specified step.
for i in itertools.count(10):
    # print(i)
    if i == 20:
        print("break")
        break

# cycle - used to cycle through an iterable indefinitely.
count = 0
for i in itertools.cycle('ABC'):
    print(i)
    count += 1
    if count == 10:
        print("break")
        break

# repeat - used to repeat an object for a specified number of times.
for i in itertools.repeat('A', 10):
    print(i)
# chain - used to combine multiple iterables into a single iterable.
for i in itertools.chain('ABC', 'DEF'):
    print(i)

# compress - used to filter elements from an iterable based on a corresponding selector iterable.
data = range(10)
selectors = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
for i in itertools.compress(data, selectors):
    print(i)

# dropwhile - used to drop elements from an iterable as long as a specified condition is true.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in itertools.dropwhile(lambda x: x < 5, data):
    print(i)

# product - used to compute the Cartesian product of input iterables.
for i in itertools.product('AB', '12'):
    print(i)

# permutations - used to generate all possible permutations of a given iterable.
for i in itertools.permutations('ABCD'):
    print(i)

# combinations - used to generate all possible combinations of a specified length from a given iterable.
for i in itertools.combinations('ABCD', 2):
    print(i)

# combinations_with_replacement - used to generate all possible combinations of a specified length from a given iterable,
# allowing for repeated elements.
for i in itertools.combinations_with_replacement('ABCD', 2):
    print(i)

# groupby - used to group consecutive elements in an iterable that have the same key value.
for key, group in itertools.groupby('AAAABBBCCDAA'):
    print(key, list(group))
#accumulate - used to compute the accumulated sums or other binary functions of elements in an iterable.
data = [1, 2, 3, 4, 5]
for i in itertools.accumulate(data):
    print(i)