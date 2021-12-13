# 최대값 찾기
# 문제 : 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

num_list = [3, 5, 6, 1, 2, 4]


# Solve First
# def solution(num_list):
#     return max(num_list)

# Solve Second
# def solution(num_list):
#     for num in num_list:
#         for num_2 in num_list:
#             if num < num_2:
#                 break
#         else:
#             return num
#     return

# Solve Third
# def solution(num_list):
#     max_num = num_list[0]
#     for num in num_list:
#         if num > max_num:
#             max_num = num

#     return max_num

# print(solution(num_list))

# == == == == == == == == == == == == == == == == == == == == == == == ==
# 최빈값 찾기
# 문제 : 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.

text = "hello my name is gunwoo"


# Solve First
# def solution(text):
#     alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     max_count = 0
#     max_alpha = alphabet_list[0]
#     for alpha in alphabet_list:
#         count = 0
#         for char in text:
#             if char == alpha:
#                 count += 1
#         if max_count < count:
#             max_count = count
#             max_alpha = alpha

#     return max_alpha

# Solve Second


# def solution(text):
#     alphabet_array = [0]*26
#     for char in text:
#         if not char.isalpha():
#             continue
#         array = ord(char) - ord('a')
#         alphabet_array[array] += 1

#     max_count = 0
#     max_alpha_index = 0
#     for index in range(len(alphabet_array)):
#         count = alphabet_array[index]

#         if count > max_count:
#             max_count = count
#             max_alpha_index = index
#     return chr(ord('a')+max_alpha_index)


# print(solution(text))


# == == == == == == == == == == == == == == == == == == == == == == == ==
# 배열에서 특정 요소 찾기

input = [3, 5, 6, 1, 2, 4]


# def solution(number):
#     if number in input:
#         return True
#     return False

# print(solution(1))

# def solution(number, array):
#     for num in array:
#         if num == number:
#             return True
#     return False


# print(solution(2, input))

# == == == == == == == == == == == == == == == == == == == == == == == ==

# 문제: 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 넣어
# 결과 적으로 가장 큰 수를 구하는 프로그램을 작성하시오.

# 단, '+'보다 'X' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.

# num_list = [0, 3, 5, 6, 1, 2, 4]


# def solution(num):
#     sum = 0
#     for i in num_list:
#         if i + sum > i*sum:
#             sum += i
#         else:
#             sum *= i
#     return sum


# print(solution(num_list))

# == == == == == == == == == == == == == == == == == == == == == == == ==
# 반복되지 않는 문자
# 문제 : 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.

text = "abadabac"


def solution(text):

    # alphabet_array = [0]*26
    # for char in text:
    #     if not char.isalpha():
    #         continue
    #     array = ord(char) - ord('a')
    #     alphabet_array[array] += 1

    # not_repeat_num = []
    # for index in range(len(alphabet_array)):
    #     alphabet = alphabet_array[index]

    #     if alphabet == 1:
    #         not_repeat_num.append(chr(index + ord('a')))
    # for char in text:
    #     if char in not_repeat_num:
    #         return char
    # return


print(solution(text))
