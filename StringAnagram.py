def stringAnagram(dictionary, query):
    # Write your code here
    amount_of_anagrams = []
    temp_query = []
    temp_dict = {}

    for word in query:
        sort = sorted(word)
        joined = "".join(sort)
        temp_query.append(joined)
    
    print(temp_query)
    for word in dictionary:
        sort = sorted(word)
        joined = "".join(sort)
        if joined in temp_dict:
            temp_dict[joined] += 1
        else:
            temp_dict[joined] = 1

    print(temp_dict)
    for target_word in temp_query:
        if target_word in temp_dict:
            amount_of_anagrams.append(temp_dict[target_word])
        else:
            amount_of_anagrams.append(0)
    
    return amount_of_anagrams