# up & down 게임 (플레이어 버전)

# **[간단설명]**

# 컴퓨터가 1~100 중에서 임의의 수를 랜덤으로 정하면, 플레이어가 해당 수를 맞히는 게임입니다.
# 컴퓨터가 정한 수가 플레이어가 말한 수보다 작으면 컴퓨터는 '업'이라고 말하고,
# 크다면 컴퓨터는 '다운'이라고 말해서 힌트를 줍니다.
# 플레이어는 힌트를 토대로 5회 안에 컴퓨터가 정한 수를 맞혀야 합니다.

# **[상세설명]**

# 1. 컴퓨터가 1~100 중에서 임의의 수(C)를 랜덤으로 정한다. (random 패키지에 있는 randrange 함수를 사용할 것)
# 2. 플레이어가 input 함수를 통해서 임의의 수(P)를 입력한다.
# 3. 컴퓨터는 C와 P를 비교하여, 업 / 다운 중 하나를 출력한다. (비교할 때는 if문을 사용할 것, '업' 혹은 '다운'은 print 문을 통해서 출력할 것)

# 업: 자신의 수(C)가 플레이어가 정한 임의의 수(P)보다 높은 경우

# 다운: 자신의 수(C)가 플레이어가 정한 임의의 수(P)보다 낮은 경우

# 1. 2~3번을 4번 더 반복한다. (즉, 2~3번을 for문으로 작성할 것)
# 2. 플레이어가 총 5회 안에 컴퓨터가 정한 수를 맞히면 '성공', 맞히지 못하면 '실패' 를 출력한다.

import random

# com_set_num = random.randrange(1, 101)


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


# # up & down 게임 (컴퓨터 버전)

# **[간단설명]**

# 플레이어가 1~100 중에서 임의의 수를 정하면, 컴퓨터가 해당 수를 맞히는 게임입니다.
# 플레이어가 정한 수가 컴퓨터가 말한 수보다 작으면 플레이어는 '업'이라고 말하고,
# 크다면 플레이어는 '다운'이라고 말해서 힌트를 줍니다.
# 컴퓨터는 플레이어가 주는 힌트를 토대로, 수를 맞힐 때까지 계속해서 시도합니다.

# **[상세설명]**

# 1. 플레이어가 input 함수를 통해서 1~100 중 임의의 수(P)를 입력한다. (1~100 이외의 수를 입력할 경우, 다시 입력하도록 할 것)
# 2. 컴퓨터는 플레이어가 정한 수(P)를 가장 빨리 맞힐 수 있도록 수(C)를 말한다. (randrange는 사용하지 말 것)
# 3. 플레이어는 C와 P를 비교하여, 업 / 다운 중 하나를 입력한다. (직접 '업' 혹은 '다운'을 input 함수를 통해 입력하도록 할 것, 그 이외의 단어를 입력할 경우 다시 입력하도록 할 것, P가 C보다 더 큰데도 플레이어가 거짓말로 '다운'이라고 할 경우에도 다시 입력하도록 할 것)

# 업: 플레이어가 정한 임의의 수(P)가 컴퓨터가 말한 수(C)보다 높은 경우

# 다운: 플레이어가 정한 임의의 수(P)가 컴퓨터가 말한 수(C)보다 낮은 경우

# 1. 2~3번을 컴퓨터가 맞힐 때까지 반복한다. (즉, 2~3번을 while문으로 작성할 것)
# 2. 컴퓨터가 수를 맞히면 '성공'을 출력한다.

def ply_up_down():
    min_num = 1
    max_num = 100

    print("숫자를 정해주세요:")
    ply_set_num = int(input())
    if not min_num <= ply_set_num <= max_num:
        print("1~100 범위의 숫자로 입력해주세요.")
        return ply_up_down()

    while True:
        com_num = min_num + ((max_num-min_num)//2)
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
