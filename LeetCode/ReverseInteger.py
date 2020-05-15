class Solution:
    def reverse(self, x: int) -> int:
        # Edge case
        if x == 0:
            return 0
        
        # Cast x to str to list; now mutable
        x_list = list(str(x))
        
        # Case 1: Negative, Case 2: Ends with 0, Base case: Positive
        if x_list[0] == "-":
            x_list.pop(0)
            x_list.reverse()
            x_list.insert(0, "-")
        elif x_list[-1] == "0":
            x_list.pop(-1)
            x_list.reverse()
        else:
            x_list.reverse()
        
        # Cast list to str to int. Return if in valid range
        reversed_x = int("".join(x_list))
        return 0 if reversed_x < -2**31 or reversed_x >= 2**31 else reversed_x