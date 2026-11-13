class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range (len(board)):
            rowhash=set()
            for j in range (len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowhash:
                    return False
                else:
                    rowhash.add(board[i][j])
        
        for i in range (len(board)):
            colhash=set()
            for j in range (len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colhash:
                    return False
                else:
                    colhash.add(board[j][i])
        
        squarehash = defaultdict(set)
        for i in range (len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                box = (i // 3) * 3 + (j // 3)
                if board[i][j] in squarehash[box]:
                    return False
                squarehash[box].add(board[i][j])
        
        return True

        


        