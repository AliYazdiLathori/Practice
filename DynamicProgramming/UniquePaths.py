class Solution:

    def calculate(self, x, y, matrix):

        if matrix[x][y] != 0:
            return matrix[x][y]

        elif x == 0:
            matrix[x][y] = self.calculate(x, y-1, matrix)
            return matrix[x][y]
        elif y == 0:
            matrix[x][y] = self.calculate(x-1,y,matrix)
            return matrix[x][y]

        matrix[x][y] = self.calculate(x-1,y,matrix) + self.calculate(x, y-1,matrix)
        return  matrix[x][y]


    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1
        return self.calculate(m-1,n-1, matrix)



if __name__ == "__main__":
    
    solution = Solution()
    print(solution.uniquePaths(3,7))
