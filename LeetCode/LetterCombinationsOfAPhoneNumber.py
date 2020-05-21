# PYTHON RECURSIVE SOLUTION
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2' : ['a', 'b', 'c' ],
            '3' : ['d', 'e', 'f' ],
            '4' : ['g', 'h', 'i' ],
            '5' : ['j', 'k', 'l' ],
            '6' : ['m', 'n', 'o' ],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v' ],
            '9' : ['w', 'x', 'y', 'z']
            }
        results = []
        if not digits:
            return results
        def helper(digit, combo=''):
            if digit:
                for letter in phone[digit[0]]:
                    helper(digit[1:], combo + letter)
            else:
                results.append(combo)
        helper(digits)
        return results

# JAVASCIPT ITERATIVE FIRST PASS
# var letterCombinations = function(digits) {
#     const phone = {
#         '2' : ['a', 'b', 'c' ],
#         '3' : ['d', 'e', 'f' ],
#         '4' : ['g', 'h', 'i' ],
#         '5' : ['j', 'k', 'l' ],
#         '6' : ['m', 'n', 'o' ],
#         '7' : ['p', 'q', 'r', 's'],
#         '8' : ['t', 'u', 'v' ],
#         '9' : ['w', 'x', 'y', 'z']
#         }
#     let ref = []
#     if (digits.length === 0){
#         return ref
#     } else if (digits.length === 1){
#         return phone[digits]
#     }
#     let first = phone[digits[0]]
#     let second = phone[digits[1]]
#     for (letter of first){
#         for (match of second){
#             ref.push(letter+match)
#         }
#     }
#     if (digits.length == 2){
#         return ref
#     }
#     let lastIndex = ref.length
#     console.log('top', lastIndex)
#     for (let i=2; i< digits.length; i++){  //DIGITS  4= g f i
#         lastIndex = ref.length
#         let currentDigit = phone[digits[i]]
#         let combo1 = currentDigit[0]
#         let combo2 = currentDigit[1]
#         let combo3 = currentDigit[2]
#         let combo4 = currentDigit[3]
#         for (let j = 0; j < lastIndex; j++){  //REF
#             ref.push(ref[j] + combo1)
#             ref.push(ref[j] + combo2)
#             ref.push(ref[j] + combo3)
#             if (combo4){
#             ref.push(ref[j] + combo4)   
#             }    
#         }
#         ref = ref.slice(lastIndex)
#     }
#     console.log('bottom', lastIndex)
#     return ref
# };