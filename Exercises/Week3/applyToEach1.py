def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, 4, 8, 9]

def absolute(a):
    return abs(a)
    
applyToEach(testList, absolute)