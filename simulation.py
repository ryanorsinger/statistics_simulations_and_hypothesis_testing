import numpy as np
import pandas as pd

# Exercise 1
# How likely is it that you roll doubles when rolling two dice?

number_of_dice_rolls = 30000
x = np.random.randint(1, 7, size=number_of_dice_rolls)
y = np.random.randint(1, 7, size=number_of_dice_rolls)

# Vanilla python solution
# count = 0
# for i, n in enumerate(x):
#     if x[i] == y[i]:
#         count += 1
# count

# idiomatic numpy solution
number_of_doubles = (x == y).sum()
probability_of_rolling_doubles = number_of_doubles / number_of_dice_rolls
print("Probability of rolling doubles is", probability_of_rolling_doubles)