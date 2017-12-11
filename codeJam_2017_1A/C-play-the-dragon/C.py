__author__ = 'pretymoon'
###################################################
#### not working yet! correct strategy, just debug!
###################################################
import math


def solve(num_debuff, num_buff):
    new_drag_hlt = dragon_health
    new_drag_atk_pow = dragon_attack_power
    new_nit_hlt = knight_health
    new_nit_atk_pow = knight_attack_power
    debuff_cnt = 0
    buff_cnt = 0
    cure_cnt = 0
    conseq_cure = 0
    num_attack = 0
    going = True
    while going:
        if new_drag_hlt <= new_nit_atk_pow - debuff_value and new_nit_hlt > new_drag_atk_pow:  ### cure
            new_drag_hlt = dragon_health - new_nit_atk_pow
            cure_cnt += 1
            conseq_cure += 1
        elif new_nit_atk_pow > 0 and debuff_cnt < num_debuff:  ### debuff
            conseq_cure = 0
            debuff_cnt += 1
            new_nit_atk_pow -= debuff_value
            if new_nit_atk_pow < 0:
                new_nit_atk_pow = 0
            new_drag_hlt -= new_nit_atk_pow
        elif new_drag_atk_pow < new_nit_hlt and buff_cnt < num_buff:  ### buff
            conseq_cure = 0
            buff_cnt += 1
            new_drag_atk_pow += buff_value
            new_drag_hlt -= new_nit_atk_pow
        else:  ### attack
            ## how many attacks before next cure?
            if new_nit_hlt > new_drag_atk_pow:
                if new_nit_atk_pow > 0:
                    n1 = new_drag_hlt // new_nit_atk_pow
                else:
                    n1 = math.ceil(new_nit_hlt/new_drag_atk_pow)
            else:
                n1 = 1
            new_nit_hlt -= n1 * new_drag_atk_pow
            if new_nit_hlt <= 0:
                new_nit_hlt = 0
                num_attack += n1
                break
            new_drag_hlt -= n1 * new_nit_atk_pow
            if new_drag_hlt <= 0:
                new_drag_hlt = 0
                num_attack += n1
                break

            # print()
            # print(new_drag_hlt, new_nit_atk_pow, n1, new_nit_hlt)
            ## how many attacks before another cure needed
            ataks_per_cure = math.ceil((dragon_health - new_nit_atk_pow)  / new_nit_atk_pow) - 1
            print("ataks_per_cure: ", ataks_per_cure)
            if new_nit_hlt > new_drag_atk_pow and ataks_per_cure == 0:
                return ["IMPOSSIBLE"]
            if new_nit_hlt > 0:
                cure_cnt += 1
                new_drag_hlt = dragon_health

                ## how many attacks before defeat?
                num_attack = math.ceil(new_nit_hlt / new_drag_atk_pow)
                new_drag_hlt -= num_attack * new_nit_atk_pow
                new_nit_hlt -= num_attack * new_drag_atk_pow
                # print("num_attack, cure_cnt, n1:    ", num_attack, cure_cnt, n1)

                ## how many more cures before defeat?
                if new_nit_hlt > 0:
                    if num_attack % ataks_per_cure == 0:
                        cure_cnt += num_attack // ataks_per_cure - 1
                    else:
                        cure_cnt += num_attack // ataks_per_cure
            # print("cure_cnt:   ", cure_cnt)
            num_attack += n1  #
            going = False

        if conseq_cure == 2:
            return ["IMPOSSIBLE"]
    return num_attack , buff_cnt , debuff_cnt , cure_cnt

ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_1A\\C-play-the-dragon\\C-small.in", "r")
# ff = open("\\Mahnaz\\PycharmProjects\\codeJam_2017_1A\\C-play-the-dragon\\C-large.in", "r")

numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    a = strLine.split(" ")
    dragon_health, dragon_attack_power, knight_health, \
    knight_attack_power, buff_value, debuff_value = [int(x) for x in a]

    n = float("inf")
    min_n = float("inf")

    debuff_step = debuff_value
    if debuff_value == 0:
        debuff_step == 1

    for i in range(0, knight_attack_power + 1):   #  knight_attack_power // (debuff_value + 1)
        for j in range(0, knight_health):  ##  knight_health // (buff_value + 1)
            ## solve(num_debuff, num_buff)
            n_arr = solve(i, j)
            print(i, j, "num_attack , buff_cnt , debuff_cnt , cure_cnt:   ", n_arr)
            # n = sum(n_arr)
            if not n_arr[0] == "IMPOSSIBLE" and sum(n_arr) < min_n:
                min_n = sum(n_arr)
    if min_n == float("inf"):
        print("IMPOSSIBLE")
    else:
        print(min_n)
