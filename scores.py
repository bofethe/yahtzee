############ Create scoring functions ############

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
    else:
        return 0
        
# 4 of a kind
def scoreFourOfKind(dice):
    freqDic = getFreqDic(dice)
    freqList = list(freqDic.values())
    if 4 in freqList:
        return sum(dice)
    else:
        return 0

# Full house (2 pair and 3 pair)
def scoreFullHouse(dice):
    freqDic = getFreqDic(dice)
    freqList = list(freqDic.values())
    if 2 in freqList and 3 in freqList:
        return 25
    else:
        return 0
    
# Small straight (3 in a row)
def scoreSmStraight(dice):
    for i in range(0,3):
        if dice[i] == dice[i+1]-1 == dice[i+2]-2:
            return 30
        else:
            return 0

# Large straight (4 in a row)
def scoreLgStraight(dice):
    for i in range(0,2):
        if dice[i] == dice[i+1]-1 == dice[i+2]-2 == dice[i+3]-3:
            return 40
        else:
            return 0
        
# Yahtzee (5 of the same)
def scoreYahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    else:
        return 0
    
# Chance (add everything)
def scoreChance(dice):
    return sum(dice)

# Get potential scores
def getScores(dice):
    d = {}
    d['1s'] = scoreOnes(dice)
    d['2s'] = scoreTwos(dice)
    d['3s'] = scoreThrees(dice)
    d['4s'] = scoreFours(dice)
    d['5s'] = scoreFives(dice)
    d['6s'] = scoreSixes(dice)
    d['3 of a Kind'] = scoreThreeOfKind(dice)
    d['4 of a Kind'] = scoreFourOfKind(dice)
    d['Full House'] = scoreFullHouse(dice)
    d['Small Straight'] = scoreSmStraight(dice)
    d['Large Straight'] = scoreLgStraight(dice)
    d['Yahtzee'] = scoreYahtzee(dice)
    d['Chance'] = scoreChance(dice)
    return d