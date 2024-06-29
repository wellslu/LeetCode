class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '0':[]}
        square_dict = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '0':[]}
        for row_index in range(len(board)):
            for col_index in range(len(board[row_index])):
                target = board[row_index][col_index]
                square = int(col_index/3) + int(row_index/3)*3
                if target != '.':
                    if board[row_index].count(target) > 1:
                        return False
                    elif target in col_dict[str(col_index)]:
                        return False
                    elif target in square_dict[str(square)]:
                        return False
                    else:
                        col_dict[str(col_index)].append(target)
                        square_dict[str(square)].append(target)
        return True
