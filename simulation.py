import numpy as np
import pandas as pd
np.random.seed(23)
# Exercise 1
# How likely is it that you roll doubles when rolling two dice?

number_of_dice_rolls = 30_000
x = np.random.randint(1, 7, size=number_of_dice_rolls)
y = np.random.randint(1, 7, size=number_of_dice_rolls)

# Vanilla python solution
# count = 0
# for i, n in enumerate(x):
#     if x[i] == y[i]:
#         count += 1
# count

# a numpy solution
# number_of_doubles = (x == y).sum()
# probability_of_rolling_doubles = (number_of_doubles / number_of_dice_rolls)
# print("Probability of rolling doubles is", probability_of_rolling_doubles)

# the 'best' numpy solution
number_of_dice_rolls = 30_000
x = np.random.randint(1, 7, size=number_of_dice_rolls)
y = np.random.randint(1, 7, size=number_of_dice_rolls)

p_doubles = (x == y).mean()
p_doubles

# a third numpy solution
rolls = np.random.randint(1, 7, (10_000, 2))
(rolls[:, 0] == rolls[:, 1]).mean()


# Exercise 2
# If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?
number_of_flips = 8
num_trials = 10_000
coin_flips = np.random.randint(0, 2, (num_trials, number_of_flips))
coin_flips
number_of_exactly_3 = 0

for flip in coin_flips:
    if flip.sum() == 3:
        number_of_exactly_3 += 1

p_exactly_3 = number_of_exactly_3 / num_trials
p_exactly_3












# Exercise 3
# There are approximitely 3 web development cohorts for every 1 data science cohort
# we randomly select an alumni to put on a billboard,
#  what are the odds that the two billboards I drive past both have data science students on them?
billboard_options = ["Web", "Web", "Web", "Data"]
x = np.random.choice(billboard_options, 10_000)    
y = np.random.choice(billboard_options, 10_000)

count_two_data_science = 0

for i, _ in enumerate(x):
    if(x[i] == "Data" and y[i] == "Data"):
        count_two_data_science += 1
    
simulated_probability = count_two_data_science / x.size
print(simulated_probability)


# Exercise 4
# students buy, on average, 3 poptart packages (+- 1.5) a day from the vending machine
# We stock 17 poptart packages on monday
# How likely is it that I will be able to buy some poptarts on Friday afternoon?

mu = 3
sigma = 1.5
s = np.random.normal(mu, sigma, 10_000)

monday_start = 17
