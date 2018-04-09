#! usr/bin/env python

"""
Given: Two positive integers k (k<=7) and N (N<=2k). In this problem, we begin
with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children
in the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.
>>> round(problem(2, 1), 3)
0.684
"""

import sys

def binomial(n, k):
    """Compute n factorial by a direct multiplicative method."""
    if k > n - k:
        k = n - k  # Use symmetry of Pascal's triangle
    accum = 1
    for i in range(1, k + 1):
        accum *= (n - (k - i))
        accum /= i
    return accum

def probability(n, k):
	
	"""
	Return the probability that there are exactly n Aa Bb offspring after k generations.

	This can be modelled as a Bernoulli trial, where success is an organism has genotype 
	Aa Bb and failure is any other genotype. Doing a Punnett square with Aa Bb and Aa Bb
	shows that probability of any offspring having that genotype is 0.25, so we use that
	as our p value.
	"""

	return binomial(2**k, n) * 0.25**n * 0.75**(2**k - n)

def num_offspring_AaBb(k, N):
	
	"""
	Return the answer to the problem.

	The trick is the "at least N" part of the problem description. Asking for "at least 1"
	is actually asking for the sum of all probabilities except for the probability that 
	the number of Aa Bb offspring is 0, and we can handle that like this:

	    1 - P(X=0)

	Where X is the random variable representing the number of offspring with the genotype Aa Bb.
	Following from this, if we want "at least 2", we should actually solve for this:

	    1 - P(X=0) - P(X=1)

	Because we want "at least N", we need a general solution with N:

	    1 - P(X=0) - P(X=1) - ... - P(X=N-1)
	"""
	offsprings = 1 - sum([probability(n, k) for n in range(N)])
	
	return offsprings

if __name__ == '__main__':
	dataset = open(sys.argv[1]).read().strip().split()
	k, N = map(int, dataset)
	print num_offspring_AaBb(k, N)
