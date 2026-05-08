class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rset = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rset:
                    rset.add(board[i][j])
                else:
                    return False
        for i in range(9):
            wset = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in wset:
                    wset.add(board[j][i])
                else:
                    return False 
        h = {}
        for i in range(9):
            h[i] = []
        for r in range(9):
            for j in range(9):
                box_idx = (r//3) * 3 + (j//3)
                if board[r][j] != ".":
                    if board[r][j] not in h[box_idx]:
                        h[box_idx].append(board[r][j])
                    else:
                        return False
        return True
            
