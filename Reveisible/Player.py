#白と黒のどちらの番であるか、白と黒それぞれがどれだけのスコアかを扱う
from Disp_field import Disp_field

class Player:
    def __init__(self):
        self.turn_flug = 1
        self.white_score = 0
        self.black_score = 0

    #配列を受け取り、その中身からスコアを算出
    def cal_score(self, field):
        self.white_score = 0
        self.black_score = 0
        for row in field:
            for i in row:
                if i == 1:
                    self.black_score+=1
                elif i == 2:
                    self.white_score+=1
                    
    def change_flug(self):
        if self.turn_flug == 1:
            self.turn_flug = 2
        else:
            self.turn_flug = 1

    def change_field(self):
        flug = self.turn_flug
        if flug == 1:
            return 1
        else:
            return 2
            
if __name__ == '__main__' :
    test = Player()
    print(test.turn_flug)
