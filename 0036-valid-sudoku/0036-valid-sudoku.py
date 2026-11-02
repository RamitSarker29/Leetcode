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
        for columns in range(len(board)) :
            seen = set()
            for rows in range(len(board)) :
                num = board[rows][columns]
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
                            nums = board[row + i][col + j]
                            if nums in seen :
                                return False
                            if nums == '.' :
                                continue
                            seen.add(nums)
        return True
