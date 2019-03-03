import os

class Disp_field:
    field = []

    def __init__(self):
        row_length = int(8)
        for i in range(row_length):
            if i == 3:
                self.field.append([0,0,0,1,2,0,0,0])
            elif i == 4:
                self.field.append([0,0,0,2,1,0,0,0])
            else:
                self.field.append([0,0,0,0,0,0,0,0])
                
    #配列を与えてそれをもとに盤を描画する関数
    def disp_field(self):
        os.system('clear')
        print('    1   2   3   4   5   6   7   8\n')
        num = 1
        field = self.field
        for i in field:
            print(str(num)+'  ', end = '')
            for j in i:
                if j == 1:
                    print('〇　', end = '')
                elif j == 2:
                    print('●　', end = '')
                else:
                    print('■　', end = '')
            print('\n')
            num+=1
            
if __name__ == '__main__':
    test = Disp_field()
    test.disp_field()
