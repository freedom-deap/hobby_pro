#座標を入力させて、置く場所を選択するやつ
#2019/02/23 後で入力の際のエラー処理について詳しく書く

class Select_locate:
    input_num = [0] * 2

    def select_locate(self, field):
        input_num = input("行番号と列番号を入力してください（例　1,1）:").split(',')
        if(len(input_num) != 2):
            print("入力の数が間違っています")
            self.select_locate(field)
        self.input_num[0] = int(input_num[0])-1
        self.input_num[1] = int(input_num[1])-1
        if self.input_num[0] >= len(field[0]) or self.input_num[1] >= len(field[0]) or self.input_num[0] < 0 or self.input_num[1] < 0:
            print("盤面の外に置こうとしています")
            self.select_locate(field)
        if field[self.input_num[0]][self.input_num[1]] != 0:
            print("その場所に置くことはできません")
            self.select_locate(field)
            
if __name__ == '__main__':
    test = Select_locate()
    test.select_locate()
    print(test.input_num)
    from Disp_field import Disp_field
    display = Disp_field()
    display.field[test.input_num[0]][test.input_num[1]] = 1
    display.disp_field()
