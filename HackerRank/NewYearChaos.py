# JAVASCIPT SOLUTION
#  function minimumBribes(arr) {
#      let largestVal = arr.length;
#      let slotWhereItGoes = largestVal - 1;
#      let bribes = 0;
#      while (largestVal > 0) {
#          let indexOfLargest = arr.indexOf(largestVal);
#          let movement = Math.abs(indexOfLargest - slotWhereItGoes);
#          if (movement > 2) {
#              console.log("Too chaotic");
#              return;
#          }
#          bribes += movement;
#          arr.splice(indexOfLargest, 1);
#          largestVal = arr.length;
#          slotWhereItGoes = largestVal - 1;
#      }
#      console.log(bribes);
# }

# BETTER SOLUTIONS
# function minimumBribes(arr) {
#     let bribes = 0;
#     for (let i = 0; i < arr.length; i++) {
#         if (arr[i] >= i + 4) {
#             console.log("Too chaotic");
#             return;
#         } else if (arr[i] -1 <= i ) {
#             for (let j = (arr[i] - 2) < 0 ? 0 : (arr[i] - 2); j < i; j++) {
#                 if (arr[i] < arr[j]) {
#                     bribes++;
#                 }
#             }
#         }
#     }
#     console.log(bribes);
# }

def minimumBribes(q):
    bribes = 0

    indexing = [num - 1 for num in q]

    for index, number in enumerate(indexing):
        if number - index > 2:
            print("Too chaotic")
            return

        for j in range(max(number-1, 0), index):
            if indexing[j] > number:
                bribes += 1
    
    print(bribes)
