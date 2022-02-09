def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [2, -3, 9, -8]

def timesAbsoluteFour(a):
    return abs(a) * abs(a)
    
applyToEach(testList, timesAbsoluteFour)