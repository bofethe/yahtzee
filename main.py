import random
import pandas as pd
import seaborn as sns
from scores import *

# Set seed for testing #TODO Remove seed before submitting
random.seed(123)

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
                                    'Three of a Kind', 'Four of a Kind',
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

            if strategy == 'upper':
                dice = roll(5)
                for i in range(0,2):
                    singles = findSingles(dice)
                    for j in singles:
                            dice[j] = random.randint(1,6)

                scores = getScores(dice)

                # Score the only category, starting with the upper section
                priority = ['1s','2s','3s','4s','5s','6s']
                scoreRecorded=False
                for k,v in specialSort(scores, priority).items():

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
                    
        # Assign 0 to the categories that were skipped due to multiple yahtzee scores
        for k in scores.keys():
            if k not in scorecard.keys():
                scorecard[k] = 0

        # Score bonus and add up the total
        if scorecard['1s'] + scorecard['2s'] + scorecard['3s'] + scorecard['4s']\
        + scorecard['5s'] + scorecard['6s'] >= 63:
            scorecard['Bonus'] = 35
        else:
            scorecard['Bonus'] = 0

        scorecard['Total'] = sum(i for i in scorecard.values())


        # keep all iterations in a single dataframe
        df_iter = pd.DataFrame.from_records(scorecard, index=[gameIter])
        df_combo = pd.concat([df_combo, df_iter])

    # Make a histogram of the total score with trendline
    sns.histplot(df_combo, x='Total', bins=50, kde=True)
    print(df_combo.describe().round(2))
    return df_combo
        

df_yahtzeeScore = playYahtzee(strategy='yahtzee', nGames=100)