import random

# Set seed for testing
random.seed(123)

# Create scorecard


# Define dice roll function
def roll(n):
    assert n <=5, f"Max of 5 dice allowed, but you tried {n}."

    dice = [random.randint(1,6) for i in range(n)]
    return dice

roll(6)