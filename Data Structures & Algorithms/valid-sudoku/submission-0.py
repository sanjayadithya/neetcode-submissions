class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for rowIndex,row in enumerate(board):

            for colIndex,num in enumerate(row):

                if num != ".":
                    # row uniqueness
                    if num in rows[rowIndex]:
                        return False
                    else:
                        rows[rowIndex].add(num)
                    
                    # column uniqueness
                    if num in cols[colIndex]:
                        return False
                    else:
                        cols[colIndex].add(num)
                    
                    # square uniqueness
                    if num in squares[(rowIndex//3,colIndex//3)]:
                        return False
                    else:
                        squares[(rowIndex//3,colIndex//3)].add(num)

        return True