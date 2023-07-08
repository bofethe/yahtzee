import random
import pandas as pd

# Set seed for testing
random.seed(123)

# Create scorecard
scoreTemplate = {'1s': None, 
                 '2s': None,
                 '3s': None,
                 '4s': None,
                 '5s': None,
                 '6s': None,
                 '3 of a Kind': None,
                 '4 of a Kind': None,
                 'Full House': None,
                 'Yahtzee': None,
                 'Chance': None}
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

# Score 1s
def scoreOnes(dice):
    n=1
    return sum([i for i in dice if i == n])

# Score 2s
def scoreTwos(dice):
    n=2
    return sum([i for i in dice if i == n])

# Score 3s
def scoreThrees(dice):
    n=3
    return sum([i for i in dice if i == n])

# Score 4s
def scoreFours(dice):
    n=4
    return sum([i for i in dice if i == n])

# Score 5s
def scoreFives(dice):
    n=5
    return sum([i for i in dice if i == n])

# Score 6s
def scoreSixes(dice):
    n=6
    return sum([i for i in dice if i == n])

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

# Full house (2 pair and 3 pair)
def scoreFullHouse(dice):
    freqDic = getFreqDic(dice)
    freqList = list(freqDic.values())
    if 2 in freqList and 3 in freqList:
        return 25
    
# Small straight (3 in a row)
def scoreSmStraight(dice):
    for i in range(0,3):
        print(i)
        if dice[i] == dice[i+1]-1 == dice[i+2]-2:
            return 30

# Large straight (4 in a row)
def scoreLgStraight(dice):
    for i in range(0,2):
        if dice[i] == dice[i+1]-1 == dice[i+2]-2 == dice[i+3]-3:
            return 40


# Yahtzee (5 of the same)
def scoreYahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    
# Chance (add everything)
def scoreChance(dice):
    return sum(dice)