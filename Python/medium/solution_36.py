# coding:utf-8
# author       : converse
# environment  : PyCharm
# created time : 2021/9/17 21:51
# version      : 3.7.2 


class Solution:
    def isValidSudoku(self, board) -> bool:
        _dict = {}
        for i in range(3):
            for j in range(3):
                _dict[str(i) + "," + str(j)] = set()

        for row_idx in range(9):
            row_container = set()
            col_container = set()
            for col_idx in range(9):

                row_element = board[row_idx][col_idx]
                col_element = board[col_idx][row_idx]

                if row_element != ".":
                    if row_element not in row_container:
                        row_container.add(row_element)
                    else:
                        return False
                if col_element != ".":
                    if col_element not in col_container:
                        col_container.add(col_element)
                    else:
                        return False

                if row_element != ".":
                    i = row_idx // 3
                    j = col_idx // 3

                    if row_element not in _dict[str(i) + "," + str(j)]:
                        _dict[str(i) + "," + str(j)].add(row_element)
                    else:
                        return False

        return True


if __name__ == '__main__':
    arr = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(arr))
