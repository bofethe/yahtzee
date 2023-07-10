import random
import pandas as pd
import seaborn as sns

# Set seed for testing #TODO Remove seed before submitting
random.seed(123)

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

############ Define Gameplay ############

# Define dice roll function
def roll(n):
    return sorted(random.randint(1,6) for i in range(n))

# Find the indexes of the dice numbers with a frequency of 1
def findSingles(dice):
    singleIndexes = []
    freqDic = getFreqDic(dice)
    for k,v in freqDic.items():
        if v == 1:
            singleIndexes.append(dice.index(k))
    return singleIndexes

# Define gameplay
def playYahtzee(strategy, nGames):
    # Make scorecard template
    df_combo = pd.DataFrame(columns=['1s','2s','3s','4s','5s','6s',
                                    '3 of a Kind', '4 of a Kind',
                                    'Small Straight', 'Large Straight', 'Full House', 
                                    'Yahtzee', 'Chance', 'Bonus', 'Total'], dtype=int)
    for gameIter in range(nGames):
        scorecard = {}

        for _ in range(13): # 13 rounds per game

            if strategy == 'yahtzee':
                dice = roll(5)
                for i in range(0,2):
                    singles = findSingles(dice)
                    for j in singles:
                            dice[j] = random.randint(1,6)

                scores = getScores(dice)
                #BUG some small and large straights arent getting picked up. Test on gameIter 248

                # Score the only category with the most points
                scoreRecorded=False
                for k,v in sorted(scores.items(), key=lambda x:x[1], reverse=True):

                    if scoreRecorded == False:

                        if k == 'Yahtzee':
                            #make sure yahtzee is alreay scored, but not 3 times yet
                            if 'Yahtzee' in scorecard.keys() and scorecard['Yahtzee'] != 150:
                                scorecard[k] += v
                                scoreRecorded=True

                            # skip if yahtzee already scored 3 times
                            elif 'Yahtzee' in scorecard.keys() and scorecard['Yahtzee'] == 150:
                                pass

                            #record new yahtzee score
                            else:
                                scorecard[k] = v
                                scoreRecorded=True

                        # score new records
                        elif k not in scorecard:

                            scorecard[k] = v
                            scoreRecorded=True

                    # skip already recorded categories
                    else:
                        pass
        # Assign 0 to the categories that were skipped due to multiple yahtzee scores
        for k in scores.keys():
            if k not in scorecard.keys():
                scorecard[k] = 0

        if scorecard['1s']+scorecard['2s']+scorecard['3s']+scorecard['4s']\
        +scorecard['5s'] +scorecard['6s'] >= 63:
            scorecard['Bonus'] = 35
        else:
            scorecard['Bonus'] = 0

        scorecard['Total'] = sum(i for i in scorecard.values())



        df = pd.DataFrame.from_records(scorecard, index=[gameIter])
        df_combo = pd.concat([df_combo, df])

    hist = sns.histplot(df_combo, x='Total', bins=50, kde=True)

    return df_combo, hist
        

df_yahtzeeScore, hist_yahtzee = playYahtzee(strategy='yahtzee', nGames=10000)

