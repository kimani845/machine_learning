# Probality is the measure of the likelihood that an event will occur.
# Probability answers a question of how do we estimate something that we are uncertain about?

#  Bayes Theorem in python. This theorem rotates about conditional probability. 
# The probability of an event A occurring given that event B has already ocured. P(A GIVEN B) or P(A|B)
#  In the examole below, a study makes a claim that 85% of cancer patients drinks coffee. P(Coffee given Cancer)

p_coffee_drinker = .65	# the percentage of the people who drank coffee
p_cancer = .005  # the percentage of people that got cancer
p_coffee_drinker_given_cancer = .85

p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer *
	p_cancer/p_coffee_drinker

# Prints 0.006538461538461539
print(p_cancer_given_coffee_drinker)

# Joint and Union Conditional Probability
p_coffee_drinker = .65	# the percentage of the people who drank coffee
p_cancer = .005  # the percentage of people that got cancer
p_coffee_drinker_given_cancer = .85

p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer *
	p_cancer

print(p_cancer_given_coffee_drinker)


# Also:
p_coffee_drinker = .65	# the percentage of the people who drank coffee
p_cancer = .005  # the percentage of people that got cancer
p_coffee_drinker_given_cancer = .85

p_coffee_drinker_given_cancer = p_cancer_drinker_given_coffee_drinker *
	p_coffee_drinker

# Prints 0.006538461538461539
print(p_cancer_given_coffee_drinker)


# BINOMIAL DISTRIBUTION
# Using sypy for the binomial distribution

from scipy.stats import binom
n = 100
p = 0.9

for k in range(n + 1 ):
	probability = binom.pmf(k,n,p)
	print("{0} - {1}".format(k, probability))
 # OUTPUT: 
# 0 - 9.99999999999996e-11
 # 1 - 8.999999999999996e-09
 # 2 - 3.644999999999996e-07
 # 3 - 8.748000000000003e-06
 # 4 - 0.0001377809999999999
 # 5 - 0.0014880347999999988
 # 6 - 0.011160260999999996
 # 7 - 0.05739562800000001
 # 8 - 0.19371024449999993
 # 9 - 0.38742048900000037
 # 10 - 0.34867844010000004