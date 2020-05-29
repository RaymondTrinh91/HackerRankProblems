def textJustification(words, L): 
        justified = []
        wordlist = []
        temp = []
        charLen = 0

        for word in words:
            if charLen + len(word) > L - len(temp):
                wordlist.append(temp)
                temp = []
                charLen = 0

            temp.append(word)
            charLen += len(word)
        wordlist.append(temp)

        for lists in wordlist[:-1]:
            string = ''
            totalSpaces = L - sum(len(word) for word in lists)
            numOfSpaces = len(lists) - 1 if len(lists) > 1 else 1
            spacing = totalSpaces // numOfSpaces
            spacingExtra = totalSpaces // numOfSpaces + 1
            remainder = totalSpaces % numOfSpaces

            if len(lists) == 1:
                string = lists[0].ljust(L)
            else:
                for i in range(len(lists)-1):
                    string += lists[i] + (' ' * (spacingExtra if i < remainder else spacing))
                string += lists[-1]

            justified.append(string)

        justified.append(' '.join(wordlist[-1]).ljust(L))
        return justified 

# FIRST PYTHON TRY 11/15
# FAILED
# def textJustification(words, maxWidth): 
#         wordlist = []
#         charLen = 0
#         justified = []
        
#         for word in words:
#             if len(word) + len(wordlist) + charLen > maxWidth:
#                 totalSpacing = maxWidth - charLen
#                 temp = []
                
#                 if len(wordlist) == 1:
#                     temp.append(wordlist[0].ljust(maxWidth))
#                 else:
#                     numOfSpaces = len(wordlist) - 1 if len(wordlist) > 1 else 1
#                     spacing = totalSpacing // numOfSpaces
#                     remainder = spacing % numOfSpaces

#                     for i in range(len(wordlist)):
#                         spaces = 0
#                         extra = 0
#                         if i != len(wordlist) - 1:
#                             remainder -= 1
#                             if remainder > 0:
#                                 extra = 1
#                             spaces = spacing + extra 
#                         temp.append(wordlist[i] + ' ' * spaces)
                        
#                 justified.append(''.join(temp))
#                 wordlist = []
#                 charLen = 0
                
#             wordlist.append(word)
#             charLen += len(word)
        
#         justified.append(' '.join(wordlist).ljust(maxWidth))
#         return justified

# FAILED JS TRY

# function textJustification(words, L) {
#     // let justified = [];
#     let wordList =[ [] ];
#     let charCount = 0
#     let arrCount = 0
#     let charCountTable = []
#     for (let i = 0; i < words.length; i++) {
#         let wordCount = wordList.length
#         // if (wordList.length == 0 && words[i].length == L){
#         //     justified.push(words[i])
#         //     wordList = []
#         //     charCount = 0
#         //     continue
#         // }
#         if(words[i].length + charCount <= (L - wordCount) ){
#             wordList[arrCount] = [...wordList[arrCount],(words[i])]
#             charCount += words[i].length
#             charCountTable[arrCount] = charCount
#             continue
#         }
#         arrCount++
#         charCount = words[i].length
#         charCountTable[arrCount] = charCount
#         wordList[arrCount] = [(words[i])]
#     }
#         //loop
#             //if current == last.  resolve as if last with funky spacing
#             //else do below functionality
#         for (let i = 0; i < wordList.length; i++){
#             let wordCount = wordList[i].length
#             let difference = L - charCountTable[i]
#             let remainderNum = difference % wordCount
#             let spacingNum = Math.floor(difference / wordCount)
#             let remainderSpaces = " ".repeat(remainderNum)
#             let spaces = " ".repeat(spacingNum)
#             if( i == wordList.length - 1) {
#                 for (let [index, string] of wordList[i].entries()){
#                 // wordList[i].forEach((string, index) =>{
#                     if (index == wordList[i].length -1){
#                         difference = L - charCountTable[i]
#                         string += " ".repeat(difference)
#                         wordList[i] = wordList[i].join("")
#                     } 
#                     else {
#                         charCountTable[i] += 1
#                         string += " "
#                     }
#                 }
#             }
#             else{
#                 for (let [index, string] of wordList[i].entries()){
#                 // wordList[i].forEach((string, index) =>{
#                     if (index == wordList[i].length -1){
#                         wordList[i] = wordList[i].join("")
#                     } 
#                     else if (index == 0) {
#                         string += remainderSpaces += spaces
#                     } 
#                     else{
#                         string += spaces
#                     }
#                 }
#             }
#         }
#         return wordList
# }