def arrayManipulation(n, queries):
    
    my_array = [0] * (n+1)
    count = 0
    temp = 0
    for first,last,value in queries:      
        my_array[first-1] += value
        my_array[last] -= value
    
    for item in my_array:
        count += item
        if count > temp:
            temp = count
            
    return temp
    # return max(itertools.accumulate(my_array))

# GEEK FOR GEEK EXPLANATION ON DIFFERNCE ARRAY
# # Python3 code to demonstrate Difference Array 
  
# # Creates a diff array D[] for A[] and returns 
# # it after filling initial values. 
# def initializeDiffArray( A): 
#     n = len(A) 
  
#     # We use one extra space because 
#     # update(l, r, x) updates D[r+1] 
#     D = [0 for i in range(0 , n + 1)] 
  
#     D[0] = A[0]; D[n] = 0
      
#     for i in range(1, n ): 
#         D[i] = A[i] - A[i - 1] 
#     return D 
  
  
# # Does range update 
# def update(D, l, r, x): 
  
#     D[l] += x 
#     D[r + 1] -= x 
  
  
# # Prints updated Array 
# def printArray(A, D): 
  
#     for i in range(0 , len(A)): 
#         if (i == 0): 
#             A[i] = D[i] 
  
#         # Note that A[0] or D[0] decides 
#         # values of rest of the elements. 
#         else: 
#             A[i] = D[i] + A[i - 1] 
  
#         print(A[i], end = " ") 
      
#     print ("") 
  
  
# # Driver Code 
# A = [ 10, 5, 20, 40 ] 
  
# # Create and fill difference Array 
# D = initializeDiffArray(A) 
# print(D)
# # After below update(l, r, x), the 
# # elements should become 20, 15, 20, 40 
# update(D, 0, 1, 10)
# print(D, "first update")
# printArray(A, D) 
  
# # After below updates, the 
# # array should become 30, 35, 70, 60 
# update(D, 1, 3, 20)
# print(D, "sec update")
# update(D, 2, 2, 30)
# print(D, "trd update")
# printArray(A, D) 