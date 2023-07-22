def specialSort(dic, priority):
    # sort priority scores
    priorityDic = sorted(priority, key=lambda key: dic[key], reverse=True)

    # sort non-prioirty scores
    otherKeys = [key for key in dic if key not in priority]
    nonPriorityKeys = sorted(otherKeys, key=lambda key: dic[key], reverse=True)

    # combine score dictionaries
    comboDic = dict([(key, dic[key]) for key in priorityDic] + [(key, dic[key]) for key in nonPriorityKeys])

    return comboDic

d = {'1s': 3, '2s': 0, '3s': 6, '4s': 8, '5s': 0, '6s':24}
prio = ['6s', '5s', '4s']

specialSort(d, prio)