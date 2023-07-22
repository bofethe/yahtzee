import random
from scores import *

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

def stratYahtzee():
    scorecard = {}
    dice = roll(5)
    for i in range(0,2):
        singles = findSingles(dice)
        for j in singles:
                dice[j] = random.randint(1,6)

    scores = getScores(dice)

    # Score the only category, starting with the most points
    scoreRecorded=False
    for k,v in sorted(scores.items(), key=lambda x:x[1], reverse=True):

        if scoreRecorded == False:

            if k == 'Yahtzee':

                #Check if yahtzee is already scored, but not 3 times yet
                if 'Yahtzee' in scorecard.keys() and scorecard['Yahtzee'] != 150:
                    scorecard[k] += v
                    scoreRecorded=True

                # skip if yahtzee already scored 3 times
                elif 'Yahtzee' in scorecard.keys() and scorecard['Yahtzee'] == 150:
                    pass

                #record first yahtzee score
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
    return scorecard