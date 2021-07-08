class WordFindErrors(Exception):
    pass
class WrongTableError(WordFindErrors):
    pass
class Game:
    def __init__(self, x:int, y:int, allowDiagonal:bool, table:list, find:list):
        self.x = x
        self.y = y
        self.digonal = allowDiagonal
        self.find = find
        self.table = table
        self.lines ={}
        if len(self.table) % x != 0 or len(self.table) % y !=0:
            raise WorngTableError
        for i in range(0, self.y):
            self.lines[i+1] = self.table[i*x:(i+1)*x]