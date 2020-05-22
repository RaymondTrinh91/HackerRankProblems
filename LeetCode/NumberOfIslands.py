class Solution:
    def dft(self, i, j, grid, height, width):
        if i < 0 or i >= height or j < 0 or j >= width or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        self.dft(i-1, j, grid, height, width)
        self.dft(i+1, j, grid, height, width)
        self.dft(i, j-1, grid, height, width)
        self.dft(i, j+1, grid, height, width)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        count = 0
        
        height = len(grid)
        width = len(grid[0])
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    count += 1
                    self.dft(i,j, grid, height, width)
                    
                    
        return count

## JAVASCRIPT FIRST PASS

# function nsew(j, i, grid) {
#     let n = grid[i - 1] ? grid[i - 1][j] : undefined;
#     let s = grid[i + 1] ? grid[i + 1][j] : undefined;
#     let e = grid[i] ? grid[i][j + 1] : undefined;
#     let w = grid[i] ? grid[i][j - 1] : undefined;
#     let c = grid[i] ? grid[i][j] : undefined;
#     if (c && Number(c)) grid[i][j] = 0;
#     if (n && Number(n)) {
#         // grid[i - 1][j] = 0;
#         nsew(j, i - 1, grid);
#     }
#     if (s && Number(s)) {
#         // grid[i + 1][j] = 0;
#         nsew(j, i + 1, grid);
#     }
#     if (e && Number(e)) {
#         // grid[i][j + 1] = 0;
#         nsew(j + 1, i, grid);
#     }
#     if (w && Number(w)) {
#         // grid[i][j - 1] = 0;
#         nsew(j - 1, i, grid);
#     }
# }
# var numIslands = function(grid) {
# // function numIslands(grid) {
#     if (grid.length == 0){
#       return 0  
#     } 
#     let height = grid.length;
#     let width = grid[0].length;
#     let islandCount = 0;
#     for (let i = 0; i < height; i++) {
#         for (let j = 0; j < width; j++) {
#             if (grid[i][j] == 1) {
#                 nsew(j, i, grid);
#                 islandCount += 1;
#             }
#         }
#     }
#     console.log(grid);
#     return islandCount;
# }function nsew(j, i, grid) {
#     let n = grid[i - 1] ? grid[i - 1][j] : undefined;
#     let s = grid[i + 1] ? grid[i + 1][j] : undefined;
#     let e = grid[i] ? grid[i][j + 1] : undefined;
#     let w = grid[i] ? grid[i][j - 1] : undefined;
#     let c = grid[i] ? grid[i][j] : undefined;
#     if (c && Number(c)) grid[i][j] = 0;
#     if (n && Number(n)) {
#         // grid[i - 1][j] = 0;
#         nsew(j, i - 1, grid);
#     }
#     if (s && Number(s)) {
#         // grid[i + 1][j] = 0;
#         nsew(j, i + 1, grid);
#     }
#     if (e && Number(e)) {
#         // grid[i][j + 1] = 0;
#         nsew(j + 1, i, grid);
#     }
#     if (w && Number(w)) {
#         // grid[i][j - 1] = 0;
#         nsew(j - 1, i, grid);
#     }
# }
# var numIslands = function(grid) {
# // function numIslands(grid) {
#     if (grid.length == 0){
#       return 0  
#     } 
#     let height = grid.length;
#     let width = grid[0].length;
#     let islandCount = 0;
#     for (let i = 0; i < height; i++) {
#         for (let j = 0; j < width; j++) {
#             if (grid[i][j] == 1) {
#                 nsew(j, i, grid);
#                 islandCount += 1;
#             }
#         }
#     }
#     console.log(grid);
#     return islandCount;
# }