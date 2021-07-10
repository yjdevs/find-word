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
        self.lines = {}
        if len(self.table) % x != 0 or len(self.table) % y !=0:
            raise WorngTableError
        for i in range(0, self.y):
            self.lines[i] = self.table[i*x:(i+1)*x]
        print(self.lines)
    def find_x(self):
        for i1 in range(0, len(self.lines)):#줄마다
            print("i1:",i1)
            for i2 in range(0, len(self.find)):#찾아야하는거 마다
                print("i2:",i2)
                forFind = self.find[i2]
                print(forFind)
                for i3 in range(0, len(self.lines[i1]) - 1):#글자 확인
                    print("i3:",i3)
                    if i3 + 1 <= len(str(forFind)):
                        print(str(self.lines[i1])[i3 + (2*(i3+1)-1)])
                        if str(self.lines[i1])[i3 + (2*(i3+1)-1)] == str(forFind)[i3]:
                            print("yeah!")
if __name__ == "__main__":
    game1 = Game(3,3,False,[1,2,3,4,5,6,7,8,9],[12,56])
    game1.find_x()