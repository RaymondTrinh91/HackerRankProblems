from decimal import *

def plusMinus(arr):
    posCount = 0
    negCount = 0
    zeroCount = 0
    for number in arr:
        if number == 0:
            zeroCount += 1
        elif number > 0:
            posCount += 1
        else:
            negCount += 1
    
    getcontext().prec = 6
    print(Decimal(posCount) / Decimal(len(arr)))
    print(Decimal(negCount) / Decimal(len(arr)))
    print(Decimal(zeroCount) / Decimal(len(arr)))