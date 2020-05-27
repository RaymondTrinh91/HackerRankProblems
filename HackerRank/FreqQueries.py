def freqQuery(queries):
    answers = []
    integers = {}
    freq = {}
    max_freq = 0

    #O(n), for n = number of tuples in queries
    for q in queries:
        # print("integer dict", integers)
        # print("frequency dict", freq)
        # print("answers", answers)

        query = q[0]
        num = q[1]

        # insert
        
        if query == 1:
            # print("insert ", num)
            if num in integers:
                integers[num] = integers[num] + 1
            
            else:
                integers[num] = 1
                # freq[integers[num]] = 1

            if integers[num] > max_freq:
                max_freq = integers[num]

        # delete
        if query == 2:
            # print("remove ", num)
            if num in integers and integers[num] > 0:
                integers[num] = integers[num] - 1
        
        # check
        if query == 3:
            # print("query ", num)
            if num <= max_freq and num in integers.values():
                answers.append(1)
            else:
                answers.append(0)

    return answers