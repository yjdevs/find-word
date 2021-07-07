class WordFindErrors(Exception):
    pass
class WorngTableError(WordFindErrors):
    pass
class Game():
    def __init__(self, x, y, allowDiagonal, table, find):
        self.x = x
        self.y = y
        self.Digonal = allowDiagonal
        self.find = find
        self.table = table
        if len(self.table) % x != 0 or len(self.table) % y !=0:
            raise WorngTableError