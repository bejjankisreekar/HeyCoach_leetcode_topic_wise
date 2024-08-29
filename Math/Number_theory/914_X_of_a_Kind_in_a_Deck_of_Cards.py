from collections import Counter
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        Determines if it's possible to group the deck of cards such that each group has the same size
        and the size is greater than 1.

        :param deck: List[int] - a list of integers representing the deck of cards.
        :return: bool - True if such grouping is possible, False otherwise.
        """
        # Step 1: Count the frequency of each unique card in the deck
        # Counter(deck) returns a dictionary where the keys are card values, and the values are their frequencies
        # .values() extracts just the frequencies, and list() converts it to a list
        count = list(Counter(deck).values())

        # Step 2: Find the greatest common divisor (GCD) of all the frequencies
        # reduce applies the gcd function cumulatively to the elements in 'count'
        # It calculates the GCD of all frequency values in the list
        all_gcd = reduce(gcd, count)

        # Step 3: Check if the GCD is greater than 1
        # If the GCD is greater than 1, it means we can group the cards into subsets where each subset has size 'X'
        # and each subset has the same size 'X'
        return all_gcd > 1



"""
1. Problem Understanding
Problem Statement: LeetCode 914, titled "X of a Kind in a Deck of Cards," asks us to determine if it's possible to divide a deck of cards into one or more groups, where:

Each group has the same number of cards.
All the cards in each group are of the same value.
In simpler terms, we are given an array of integers where each integer represents a card, and we need to check if we can partition the array into groups with identical card values and the same group size.

Inputs and Outputs:

Input: An array of integers, deck, where each integer represents a card.
Output: A boolean value, True if it is possible to divide the deck as described, otherwise False.
Constraints:

The length of deck will be between 1 and 10000.
The values in deck are non-negative integers that represent different types of cards.
Special Conditions:

The group size must be at least 2.
2. Initial Thoughts and Intuition
First Considerations:

The problem requires grouping identical elements. To do this, counting the occurrences of each card is necessary.
The key is to find a common divisor (greater than 1) for all the counts, which would allow us to divide the deck into groups of that size.
Obvious Solutions:

Counting the frequency of each card type and checking if the greatest common divisor (GCD) of these counts is greater than 1 seems like a promising approach.
Simplification:

Visualizing the problem: Imagine dividing a deck of 52 cards into groups where each group has the same type of card and the same number of cards. The goal is to ensure the number of cards in each group is a divisor of the total count.
3. Core Concepts and Prerequisites
Fundamental Concepts:

Frequency Counting: We need to count how many times each unique card appears in the deck.
Greatest Common Divisor (GCD): The GCD is essential here. The GCD of the card frequencies will determine the largest possible group size.
Refresher on GCD:

The GCD of two numbers is the largest number that divides both without leaving a remainder. For example, the GCD of 8 and 12 is 4.
4. Brute Force Approach
Brute Force Logic:

Count the frequency of each card.
Try every possible group size starting from 2 up to the smallest count of any card. For each group size, check if all counts are divisible by this size.

Complexity Analysis:

Time Complexity: O(N * sqrt(M)), where N is the number of unique cards, and M is the minimum frequency.
Space Complexity: O(N) for storing the card frequencies.
Limitations:

This approach may be inefficient for large decks or decks with many unique cards, as it checks every possible group size.
5. Optimized Solution
Optimized Approach:

Instead of checking every possible group size, calculate the GCD of all card frequencies. If the GCD is greater than 1, then we can divide the deck into groups of that size.
Algorithmic Strategy:

Use Python's math.gcd function to compute the GCD of the card frequencies.
Reduce the problem to checking if the GCD of all frequencies is greater than 1.

Complexity Analysis:

Time Complexity: O(N log K), where N is the number of unique cards, and K is the maximum frequency. The reduce function applies the GCD operation across the frequencies.
Space Complexity: O(N) for storing the card frequencies.
Comparison with Brute Force:

The optimized solution is significantly faster, especially for large decks, as it avoids checking each possible group size.
6. Step-by-Step Code Walkthrough
Code Breakdown:

Counter(deck): Counts the occurrences of each card in the deck.
list(Counter(deck).values()): Converts the frequency dictionary into a list of counts.
reduce(gcd, count): Computes the GCD of the list of counts.
gcd_all > 1: Checks if the computed GCD allows us to form valid groups.

"""