def diagonalDifference(arr):
    first = 0
    second = 0

    forwards = 0
    backwards = len(arr[0])-1
    for i in range(len(arr)):
        first += arr[i][forwards]
        second += arr[i][backwards]

        forwards += 1
        backwards -= 1
    
    print(first)
    print(second)
    return abs(first - second)