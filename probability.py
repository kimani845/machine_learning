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

