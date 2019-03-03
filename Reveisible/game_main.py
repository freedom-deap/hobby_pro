from Disp_field import Disp_field
from Select_locate import Select_locate
from Player import Player
from main_function import judge_field, judge_select_locate
from time import sleep

#ここで他の関数を呼んで動かす
if __name__ == '__main__':
    turn = 1
    display = Disp_field()
    select = Select_locate()
    player = Player()
    display.disp_field()
    while(True):
        if turn > 1:
            if judge_select_locate(display.field, player.turn_flug) == 0:
                print("置ける場所がありません")
                sleep(1)
                continue
        select.select_locate(display.field)
        display.field[select.input_num[0]][select.input_num[1]] = player.change_field()
        judge_field(display.field, select.input_num[0], select.input_num[1], player.turn_flug)
        player.change_flug()
        display.disp_field()
