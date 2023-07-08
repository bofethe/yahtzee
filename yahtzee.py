import random
import pandas as pd

# Set seed for testing
random.seed(123)

# Create scorecard


# Define dice roll function
def roll(n):
    assert n <=5, f"Max of 5 dice allowed, but you tried {n}."

    return [sorted(random.randint(1,6) for i in range(n))]

### Create scoring functions
# Get dictionary of distinct counts
def getFreqDic(dice):
    freqDic = {}
    for i in dice:
        if i in freqDic:
            freqDic[i] += 1
        else:
            freqDic[i] = 1
    return freqDic

# 3 of a kind
def scoreThreeOfKind(dice):
    freqDic = getFreqDic(dice)
    freqList = list(freqDic.values())
    if 3 in freqList:
        return sum(dice)
        
# 4 of a kind
def scoreFourOfKind(dice):
    freqDic = getFreqDic(dice)
    freqList = list(freqDic.values())
    if 4 in freqList:
        return sum(dice)

# Full house
def scoreFullHouse(dice):
    freqDic = getFreqDic(dice)
    freqList = list(freqDic.values())
    if 2 in freqList and 3 in freqList:
        return 25
    
# Small straight
def scoreSmStraight(dice):
    for i in range(0,3):
        print(i)
        if dice[i] == dice[i+1]-1 == dice[i+2]-2:
            return 30

# Large straight
def scoreLgStraight(dice):
    for i in range(0,2):
        if dice[i] == dice[i+1]-1 == dice[i+2]-2 == dice[i+3]-3:
            return 40


# Yahtzee 
def scoreYahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    
# Chance
def scoreChance(dice):
    return sum(dice)

scoreThreeOfKind([3,3,3,1,5])