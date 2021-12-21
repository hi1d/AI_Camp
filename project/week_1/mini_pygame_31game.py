# 베스킨라빈스 31 게임
import random
# - **[간단설명]**

# 1부터 31까지의 숫자를 플레이어와 컴퓨터가 번갈아 가면서 순서대로 말합니다.
# 숫자를 말할 때는 1개부터 3개까지의 연속된 숫자를 말할 수 있습니다.
# 즉, 처음 시작하는 사람이 무조건 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 시작하고,
# 그 뒷 사람은 앞 사람이 말한 숫자에 이어서 또 1개\~3개의 연속된 숫자를 차례대로 말하는 방식입니다.
# (앞 사람이 3까지 불렀다면, 뒷 사람은 4 혹은 4, 5 혹은 4, 5, 6을 말해야 합니다.)
# 그렇게 해서 31을 부르는 사람이 지는 게임입니다.

# - **[상세설명]**

# 1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.

# 2. 컴퓨터 혹은 플레이어는 1 혹은 1, 2 혹은 1, 2, 3을 말하면서 게임을 시작한다. (단, 컴퓨터가 숫자를 1개 부를지, 2개 부를지, 3개 부를지는 random 패키지를 이용해서 랜덤으로 정한다. 플레이어는 input 함수를 통해서 연속해서 부르고 싶은 숫자 개수를 입력한다.)

# 3. 컴퓨터 혹은 플레이어는 앞 사람이 부른 숫자에 이어서, 1개~3개까지의 연속된 숫자를 말한다.

# 4. 2\~3번을 31을 말하는 사람이 나올 때까지 반복한다. (즉, 2\~3번을 for문 혹은 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)

# 5. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을, 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.

# (가능하다면, 컴퓨터가 숫자를 뽑는 코드와 플레이어가 숫자를 뽑는 코드는 함수화를 해보세요!)

# turn = random.randint(0, 1)
# # turn 0 = Player Trun
# # turn 1 = Computer Turn
# global number
# global Flag
# number = 0
# Flag = True


# def player_input():
#     count = int(input("시행 횟수: "))
#     if count > 3:
#         print("1~3안의 범위로 입력해주세요.")
#         player_input()
#     return count


# def player_turn(count):
#     global number
#     global Flag
#     for i in range(count):
#         number += 1
#         print(f"플레이어 현재 숫자 : {number}")

#         if number > 30:
#             print("컴퓨터 승")
#             Flag = False
#             return True
#     return False


# def computer_turn():
#     global number
#     global Flag
#     count = random.randint(1, 3)
#     for i in range(count):
#         number += 1
#         print(f"컴퓨터 현재 숫자 : {number}")

#         if number > 30:
#             print("플레이어 승")
#             Flag = False
#             return True
#     return False


# while Flag:
#     if turn == 0:
#         count = player_input()
#         if player_turn(count):
#             break
#         computer_turn()
#     else:
#         if computer_turn():
#             break
#         count = player_input()
#         player_turn(count)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 베스킨라빈스 31 인공지능 만들기

# - **[간단설명]**

# 앞서 본 게임과 규칙은 동일하지만, 이번에는 플레이어가 어떤 식으로 숫자를 부르든,
# 컴퓨터는 항상 자신이 이기도록 나름의 방식의 가지고 숫자를 부릅니다.
# (그 방식이 무엇인지는 검색을 해보아도 좋고, 직접 생각해보셔도 좋습니다.
# *'항상'이라고 명시했지만, 딱 한 가지 경우에는 컴퓨터가 질 수도 있습니다.)

# - **[상세설명]**

# 1. 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.

# 2. 기존의 게임과 마찬가지로 1부터 순서대로 연속된 숫자를 말하되,
# 플레이어는 input 함수를 통해서 부르고 싶은 숫자까지 이어서 말한다.
# 컴퓨터는 나름의 방식을 가지고 숫자를 말한다.

# 3. 2번 과정을 31을 말하는 사람이 나올 때까지 반복한다.
# (즉, 2번을 for문 혹은 while문으로 작성할 것. 단, 컴퓨터와 플레이어 모두 31을 초과해서 숫자를 부를 수는 없다.)

# 4. 31을 말하는 사람이 컴퓨터라면 '플레이어 승'을,
# 31을 말하는 사람이 플레이어라면 '컴퓨터 승'을 출력한다.
# (단, 컴퓨터는 자신이 항상 이기도록 나름의 방식을 가지고 숫자를 부르기 때문에,
# 딱 한 가지 경우를 제외하고는 항상 컴퓨터가 이길 수 밖에 없을 것임에 유의)

# (가능하다면, 컴퓨터가 숫자를 뽑는 코드와 플레이어가 숫자를 뽑는 코드는 함수화를 해보세요!)

turn = random.randint(0, 1)
# turn 0 = Player Trun
# turn 1 = Computer Turn
global number
global Flag
number = 0
Flag = True


def player_input():
    count = int(input("시행 횟수: "))
    if count > 3:
        print("1~3안의 범위로 입력해주세요.")
        player_input()
    return count


# 2 6 10 14 18 22 26 30
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# 1 2 3 0 1 2 3 0 1 2  3  0  1  2  3  0  1  2  3  0  1  2  3  0  1  2  3  0  1  2
# number % 4 == 2 면 이김.

def computer_count():
    global number
    if number % 4 == 1:
        length = 1
    if number % 4 == 2:
        length = random.randint(1, 3)
    if number % 4 == 3:
        length = 3
    if number % 4 == 0:
        length = 2

    return length


def player_turn(count):
    global number
    global Flag
    for i in range(count):
        number += 1
        print(f"플레이어 현재 숫자 : {number}")

        if number > 30:
            print("컴퓨터 승")
            Flag = False
            return True
    return False


def computer_turn():
    global number
    global Flag
    count = computer_count()
    for i in range(count):
        number += 1
        print(f"컴퓨터 현재 숫자 : {number}")

        if number > 30:
            print("플레이어 승")
            Flag = False
            return True
    return False


while Flag:
    if turn == 0:
        count = player_input()
        if player_turn(count):
            break
        computer_turn()
    else:
        if computer_turn():
            break
        count = player_input()
        player_turn(count)
