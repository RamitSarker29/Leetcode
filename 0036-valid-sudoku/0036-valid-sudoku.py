class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)) :
            seen = set()
            for j in board[i] :
                if j == '.' :
                    continue
                if j in seen :
                    return False
                seen.add(j)
        for col in range(len(board)) :
            seen = set()
            for row in range(len(board)) :
                num = board[row][col]
                if num == '.' :
                    continue
                if num in seen :
                    return False
                seen.add(num)
        for col in range(0 , 9 , 3) :
            for row in range(0 , 9 , 3) :
                seen = set()
                for i in range(3) :
                    for j in range(3) :
                        num = board[row + i][col + j]
                        if num == '.' :
                            continue
                        if num in seen :
                            return False
                        seen.add(num)
        return True
 


        