def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for key, value in aDict.items():
        count += len(value)
    return count

print(how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}))