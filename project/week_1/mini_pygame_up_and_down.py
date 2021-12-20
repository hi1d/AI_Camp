# up & down 게임 (플레이어 버전)

import random
import sys


# com_set_num = random.randrange(1, 100)


# def com_up_down(com_set_num):
#     for i in range(5):
#         print("숫자를 입력하세요:")
#         num = int(input())
#         if num == com_set_num:
#             return print("정답")
#         elif num > com_set_num:
#             print("다운")
#         elif num < com_set_num:
#             print("업")
#     return print("실패")


# com_up_down(com_set_num)


# up & down 게임 (컴퓨터 버전)

def ply_up_down():
    min_num = 1
    max_num = 100

    print("숫자를 정해주세요:")
    ply_set_num = int(input())
    if not min_num < ply_set_num < max_num:
        print("1~100 범위의 숫자로 입력해주세요.")
        return ply_up_down()

    while True:
        com_num = min_num + ((max_num-min_num) // 2)
        print(com_num)
        if com_num == ply_set_num:
            return print("성공")
        elif com_num > ply_set_num:
            ply_input = str(input())
            while ply_input != "다운":
                print("다시 입력 하세요.")
                ply_input = str(input())
            max_num = com_num - 1
        else:
            ply_input = str(input())
            while ply_input != "업":
                print("다시 입력 하세요.")
                ply_input = str(input())
            min_num = com_num + 1
    return


ply_up_down()
