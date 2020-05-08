class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split('')
        array = list(reversed(array))
        string = ' '.join(array)
        stripped_string = ' '.join(string.split())
        return stripped_string


# var reverseWords = function(s) {
#     let arr = s.split(" ")
#     arr.reverse()
#     string = arr.join(" ")
#     string = string.replace(/\s+/g, ' ')
#     return string.trim()
# };

# var reverseWords = function (s) {
#     let arr = s.split(" ");
#     arr.reverse();
#     let string = arr.filter((item) => item != "").join(" ");
#     return string;
# };