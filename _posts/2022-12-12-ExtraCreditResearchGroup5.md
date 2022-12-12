---
toc: true
layout: post
description: Binary Search Research Paper (Extra Credit)
categories: [markdown]
title: Binary Search Research Paper (Extra Credit)
---


# BINARY SEARCH ALGORITHM RESEARCH

The performance of linear search algorithm can be realized when the number of element is too large. In such situation binary search algorithm is quite useful. The binary search algorithm can be applied to an array whose elements are to be required in sorted form. Each iteration of binary search narrows the search interval by half of the search interval of its previous iteration. The time required by binary search is O (log2 N). Variation of binary search can be possible by selecting a random element between lower and upper bound.Function BINARY_SEARCH(K, N, X) : Given a vector K,consisting of N elements in ascending order, this algorithm
searches the structure for a given element whose value is given by X. The variables LOW, MIDDLE and HIGH denote the lower, middle and upper limits of the search interval. The function returns the index of the vector element if the search is successful and returns 0 otherwise.

1. [Initialize]
LOW ← 1
HIGH ← N
2. [Perform search]
Repeat thru step 4 while LOW ≤ HIGH
3. [Obtain index of midpoint of interval]
MIDDLE ← (LOW + HIGH) / 2
4. [Compare]
If X < K [MIDDLE]
then HIGH ← MIDDLE – 1
else If X > K [MIDDLE]
 then LOW ← MIDDLE + 1

elseWrite(‘SUCCESSFULSEARCH’)
 Return (MIDDLE)
5. [Unsuccessful search)
Write(‘UNSUCCESSFULSEARCH’)
Return (0)


Above algorithm searches an element X by first examining
the center element of the vector K. If it is found then search
process is completed otherwise it will check for the element
whether exist in first half or the second half by testing the
condition. If X < K[MIDDLE] then element might be in first
half so the upper limit of the next interval is changed by
MIDDLE – 1. If X > K[MIDDLE] then element might be
found in second half of the current interval so the lower limit
is changed by MIDDLE + 1. This process continues until
LOW <= HIGH