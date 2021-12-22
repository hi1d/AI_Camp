# # 간단한 턴제 RPG
# **[간단설명]**

# 여러분은 간단한 턴제 RPG 게임을 만들고자 합니다. 이 RPG 게임에서는 '몬스터'와 '플레이어' 가 각각 존재하고,
# 모두 이름/HP/공격력이라는 공통 속성을 가지고 있습니다.
# 몬스터와 플레이어는 각각 자신의 차례가 오면 일정한 행동을 할 수 있습니다.
# '플레이어'는 자신의 턴이 오면, '몬스터'를 상대로 '공격'을 할수도 있고, '마법'을 사용할 수도 있습니다.
# '몬스터'는 자신의 턴이 오면, '플레이어'를 상대로 '공격'을 할 수도 있고, 그냥 자신의 체력을 회복할 수도 있고,
# 그냥 아무 행동도 안할 수 있습니다. 플레이어와 몬스터 모두 자신의 턴에 여러 개의 행동을 한번에 할 수는 없고,
# 딱 하나의 행동만을 선택할 수 있습니다.

# 현재 상황은 '전사'와 '미니고블린', '고블린', '슈퍼고블린'이 1대3으로 대치하는 상황입니다.
# 위 설명을 기반으로, 플레이어가 '전사'를 조작해서 3마리의 몬스터와 싸우도록 게임을 구현해보세요.

# **[상세설명]**

# 큰 틀에서의 프로세스 다음과 같습니다.

# 1. '플레이어'와 '몬스터'라는 클래스를 만들고, 각각이 할 수 있는 행동을 메소드(함수) 형태로 클래스 내부에서 정의한다.
# 2. 플레이어가 입력하는 값에 따라 플레이어 클래스 내부의 함수 (공격, 마법) 가 실행되도록 하는 '플레이어 턴'이라는 함수와,
# 랜덤으로 몬스터 클래스 내부의 함수가 실행되도록 하는 '몬스터 턴'이라는 함수를 정의한다.
# 3. 두 함수를 While 문 아래에 배치해서, 모든 몬스터가 죽거나, 플레이어가 죽기 전까지는 계속 턴이 번갈아가며 진행되도록 한다.

# **[상세설명 - 1. 클래스 생성 파트]**

# 여기서 '플레이어'와 '몬스터'는 모두 Object 라는 공통된 클래스를 상속받아서 만들어진 클래스입니다.

# 1. Object 클래스는 '이름', 'HP', '공격력'이라는 속성과 '공격'이라는 메소드를 가지고 있습니다.

# (공격이라는 함수는 '공격하고자 하는 대상'을 인자로 받으며, 실행할 경우, 공격하고자 하는 대상의 HP를 자신의 공격력만큼 감소시킵니다. 공격할 때에는 ~~가 ~~를 공격했고, 그에 따라 공격받은 대상의 체력이 얼마 남았는지가 print 문으로 출력됩니다.)

# 1. Player 클래스는 Object 클래스를 상속받으며, '마법'이라는 메소드를 가지고 있습니다.

# (마법이라는 함수는 '공격하고자 하는 대상'을 인자로 받으며, 실행할 경우, 공격하고자 하는 대상의 HP를 50만큼 감소시킵니다. 공격할 때에는 ~~가 ~~를 공격했고, 그에 따라 공격받은 대상의 체력이 얼마 남았는지가 print 문으로 출력됩니다.)

# 1. Monster 클래스는 Object 클래스를 상속받으며, '대기'와 '치료'라는 메소드를 가지고 있습니다.

# (대기라는 함수는 self 외에는 다른 인자를 받지 않으며, 그냥 "~~가 대기했습니다" 만 출력됩니다.)

# (치료라는 함수는 self 외에는 다른 인자를 받지 않으며, 자기 자신의 HP를 10 증가시키는 기능을 가지고 있습니다. 증가시킬 때는 "~~가 자신의 체력을 10만큼 회복했다" 가 출력됩니다.)

# **[상세설명 - 2. 함수 생성 파트]**

# 1. 전사는 Player 클래스의 인스턴스로서, 100의 체력, 10의 공격력을 가지고 있습니다.
# 2. 고블린들은 모두 Monster 클래스의 인스턴스로서, 미니고블린은 10의 체력과 10의 공격력을,
# 고블린은 30의 체력과 30의 공격력을, 슈퍼고블린 50의 체력과 50의 공격력을 가지고 있습니다.
# 3. 정보 표시 함수 : 턴이 시작하기 전에, 우선은 해당 턴을 시작할 때 전사와 고블린들의 체력이 얼마인지를 표시합니다.
# (단, 이미 체력이 0이 되어서 죽은 고블린의 체력은 표시하지 않습니다.)
# 4. 플레이어 턴 함수 : 전사의 행동 (공격/마법 + 그 대상) 은 Input 에 따라 이루어집니다.
# 사용자한테 공격을 선택할지, 마법을 선택할지를 input 함수로 물어보고, 누구를 공격할지 또한 Input 함수로 물어봅니다.
# 그러면 그 input 값을 토대로 전사는 하나의 몬스터를 대상으로 공격을 하거나 마법을 사용합니다.
# (오늘 실습은 작성할 코드 자체가 많으므로, input 값에 따른 예외처리는 아예 하지 않는 것을 권장합니다!)
# 5. 몬스터 사망 여부 체크 함수 : 플레이어 턴이 끝났을 때, 체력이 0 이하인 몬스터가 있다면
# 해당 몬스터는 앞으로 정보가 표시되지 않도록 하는 작업을 진행합니다.
# 여기서 사망 여부를 체크했더니, 모든 몬스터가 다 사망했다면, 함수 밖에서 '승리' 를 출력하고 While 문을 빠져나오도록 작성합니다. (즉, 게임을 종료)
# 6. 몬스터 턴 함수 : 몬스터의 행동 (치료, 대기, 공격) 은 랜덤하게 이루어집니다.
# 모든 몬스터는 각각 랜덤하게 하나의 행동을 실행합니다. (즉, 몬스터 턴에서는 몬스터 3마리 각각 하나의 행동을 실행해야 합니다. 몬스터 중 1마리만 행동을 실행하고 턴이 넘어가는 것이 아닙니다!)
# 7. 플레이어 사망 여부 체크 함수 : 몬스터 턴이 끝났을 때,
# 플레이어의 체력이 0 이하라면 함수 밖에서 '패배'를 출력하고 While 문을 빠져나오도록 작성합니다.

# **[상세설명 - 3. 게임 실행 파트]**

# 1. 앞서 만든 함수들을 순서대로 While 문 안에 배치합니다.

import random
import time


class Object:
    gamestate = True

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        target.hp -= self.damage
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
        print(f"{target.name}의 HP : {target.hp}")

    def info(self):
        print(f"{self.name} HP : {self.hp} ")


class player(Object):

    def magic(self, target):
        target.hp -= 50
        print(f"{self.name}이(가) {target.name}을(를) 마법 공격!")
        print(f"{target.name}의 HP : {target.hp}")

    def playerTurn(self):
        player_action = input("공격/마법 : ")
        if player_action != '공격' and player_action != '마법':
            print("공격 또는 마법을 입력해주세요.")
            self.playerTurn()
        Target_state = True
        while Target_state:
            player_target = input("대상 : ")
            if player_target in monster.monster_list:
                Target_state = False
            else:
                print("대상이 없습니다.")

        if player_action == "공격":
            self.attack(monster.monster_list[player_target])
        elif player_action == "마법":
            self.magic(monster.monster_list[player_target])
        monster.monster_list[player_target].monsterAlive()

    def playerAlive(self):
        if self.hp <= 0:
            print("패배...")
            Object.gamestate = False


class monster(Object):
    monster_list = {}

    def wait(self):
        print(f"{self.name}이(가) 대기했습니다.")

    def heal(self):
        self.hp += 10
        print(f"{self.name}이(가) 자신의 체력을 10만큼 회복했다.")

    def monsterTurn(self):
        rand_count = random.randint(0, 2)
        if rand_count == 0:
            self.heal()
        elif rand_count == 1:
            self.wait()
        elif rand_count == 2:
            self.attack(전사)
        전사.playerAlive()

    def monsterAlive(self):
        if self.hp <= 0:
            del monster.monster_list[self.name]
            print(f"{self.name} 사망!")
        if len(monster.monster_list) == 0:
            print("승리!")
            Object.gamestate = False


전사 = player("전사", 100, 10)
미니고블린 = monster("미니고블린", 10, 10)
monster.monster_list['미니고블린'] = 미니고블린
고블린 = monster("고블린", 30, 30)
monster.monster_list['고블린'] = 고블린
슈퍼고블린 = monster("슈퍼고블린", 50, 50)
monster.monster_list['슈퍼고블린'] = 슈퍼고블린

while Object.gamestate:

    print('--------------정보-----------------')
    전사.info()
    for i in monster.monster_list:
        monster.monster_list[i].info()
    print('----------------------------------')
    전사.playerTurn()
    print('----------------------------------')
    for i in monster.monster_list:
        time.sleep(2)
        monster.monster_list[i].monsterTurn()
