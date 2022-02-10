def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = None
    for key in aDict.keys():
        if biggest is None or len(aDict[key]) > len(aDict[biggest]) :
            biggest = key
     
    return biggest