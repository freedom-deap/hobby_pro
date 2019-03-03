#盤上の石をひっくり返すためのやつ
import time

'''
テンキーの配置でそれぞれの方向を表し、
配列の中身で配列の中身をどう見ていくかを表す
judge_vec1 = [-1,1]
judge_vec2 = [0,1]
judge_vec3 = [1,1]
judge_vec4 = [-1,0]
judge_vec5 = [0,0]
judge_vec6 = [1,0]
judge_vec7 = [-1,-1]
judge_vec8 = [0,-1]
judge_vec9 = [1,-1]
'''
judge_vec = [[1,-1], [1,0], [1,1], [0,-1], [0,0], [0,1], [-1,-1], [-1,0], [-1,1]]

#ひっくり返せる石の判定と石の操作
def judge_field(field, locate_x, locate_y, turn_flug):
    if locate_y < 2:
        if locate_x < 2:
            judge_one_direction(field, locate_x, locate_y, judge_vec[1], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[2], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[5], turn_flug)
        elif locate_x < 7:
            judge_one_direction(field, locate_x, locate_y, judge_vec[1], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[2], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[5], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[7], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[8], turn_flug)
        else:
            judge_one_direction(field, locate_x, locate_y, judge_vec[5], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[7], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[8], turn_flug)
    elif locate_y < 7:
        if locate_x < 2:
            judge_one_direction(field, locate_x, locate_y, judge_vec[0], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[1], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[2], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[3], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[5], turn_flug)
        elif locate_x < 7:
            judge_one_direction(field, locate_x, locate_y, judge_vec[0], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[1], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[2], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[3], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[5], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[6], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[7], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[8], turn_flug)
        else:
            judge_one_direction(field, locate_x, locate_y, judge_vec[3], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[5], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[6], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[7], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[8], turn_flug)
    else:
        if locate_x < 2:
            judge_one_direction(field, locate_x, locate_y, judge_vec[0], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[1], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[3], turn_flug)
        elif locate_x < 7:
            judge_one_direction(field, locate_x, locate_y, judge_vec[0], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[1], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[3], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[6], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[7], turn_flug)
        else:
            judge_one_direction(field, locate_x, locate_y, judge_vec[3], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[6], turn_flug)
            judge_one_direction(field, locate_x, locate_y, judge_vec[7], turn_flug)
            
#1～9のうち与えられた方向に判定を行う
def judge_one_direction(field, locate_x, locate_y, j_vec, turn_flug):
    #print(j_vec)
    #time.sleep(3)
    judge_locate = turn_flug
    judge_count = cal_count(field, locate_x, locate_y, j_vec, turn_flug)
    x, y = locate_x, locate_y
    for i in range(judge_count):
        #print('revirsing now')
        #time.sleep(1)
        x+=j_vec[0]
        y+=j_vec[1]        
        field[x][y] = judge_locate
        
def cal_count(field, locate_x, locate_y, j_vec, turn_flug):
    x, y = locate_x, locate_y
    judge_count = 0
    judge_locate = turn_flug
    x+=j_vec[0]
    y+=j_vec[1]
    next_locate = field[x][y]
    if judge_locate != next_locate or next_locate != 0:
        while(next_locate != judge_locate):
            if next_locate == 0:
                judge_count = 0
                break
            judge_count += 1
            x += j_vec[0]
            y += j_vec[1]
            if x == -1 or x == 8 or y == -1 or y == 8:
                judge_count = 0
                break
            next_locate = field[x][y]
            #print(judge_count)
            #time.sleep(1)
    return judge_count

#その時のプレイヤーに置く場所が存在しているかを判定
def judge_select_locate(field, player_flug):
    for i in range(8):
        locate_x = i
        for j in range(8):
            judge_count = 0
            locate_y = j
            if field[locate_x][locate_y] != 0:
                continue
            if locate_y < 2:
                if locate_x < 2:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[1], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[2], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[5], player_flug)
                elif locate_x < 7:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[1], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[2], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[5], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[7], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[8], player_flug)
                else:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[5], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[7], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[8], player_flug)
            elif locate_y < 7:
                if locate_x < 2:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[0], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[1], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[2], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[3], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[5], player_flug)
                elif locate_x < 7:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[0], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[1], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[2], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[3], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[5], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[6], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[7], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[8], player_flug)
                else:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[3], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[5], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[6], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[7], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[8], player_flug)
            else:
                if locate_x < 2:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[0], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[1], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[3], player_flug)
                elif locate_x < 7:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[0], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[1], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[3], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[6], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[7], player_flug)
                else:
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[3], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[6], player_flug)
                    judge_count+=cal_count(field, locate_x, locate_y, judge_vec[7], player_flug)
                    
    if judge_count > 0:
        return 1
    else:
        return 0
