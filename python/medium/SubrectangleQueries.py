class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.graphic = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        col = col1
        while row1 <= row2:
            while col <= col2:
                self.graphic[row1][col] = newValue
                col+=1
            col = col1
            row1+=1
        return None
        

    def getValue(self, row: int, col: int) -> int:
        return self.graphic[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
