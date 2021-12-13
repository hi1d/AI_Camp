# 삼항연산자
num = 3

result = ('짝수' if num % 2 == 0 else '홀수')


print(f'{num}은 {result}입니다.')

# For문 한줄로 표현하기

a_list = [1, 3, 2, 5, 1, 2]
b_list = []

b_list = [a*2 for a in a_list]

print(b_list)

# map 함수

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]


def check_adult(person):
    return '성인' if person['age'] > 20 else '청소년'


result = list(map(check_adult, people))
print(result)

# 람다식 : 함수를 한줄로 표현하는 식
result = list(
    map(lambda x: ('성인' if x['age'] > 20 else '청소년'), people))
print(result)

# filter : True인 것들만 뽑기, 직관적
result = list(filter(lambda x: x['age'] > 20, people))
print(result)

# 클래스 :


class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp -= attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive == True:
            print("살았다.")
        else:
            print("죽었다.")


m1 = Monster()
m1.damage(150)
m1.status_check()

m2 = Monster()
m2.damage(90)
m2.status_check()
