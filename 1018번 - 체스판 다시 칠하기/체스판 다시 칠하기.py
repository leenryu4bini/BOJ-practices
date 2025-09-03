#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1018                           #+#        #+#      #+#     #
#    Solved: 2025/08/10 17:34:21 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

#자르는 게 문제일 듯.
#추가적으로 칠해야 하는 게 젤 적게 8*8 모양을 잘라야 한다니...

# 왼쪽 최상단의 값이 b일 때/ w일 때의 이상적인 체스판을 구성해두고 이거와의 차이가 적은 것을 찾아 봐야 한다..


#입력 받기
row, col= map(int, input().split())

ipt_chess=[]

for _ in range(row):
    a= input()
    ipt_chess.append(a)
print("\n".join(ipt_chess))
print('------------')

#이상적인 체스판 만들기

def make_chess(version, row, col):
    if version == 1:
        first, second = 'W', 'B'
    elif version == 2:
        first, second = 'B', 'W'

    # col 길이의 패턴 두 줄 만들기
    # (first+second) 패턴 반복한 뒤 슬라이싱
    base = (first + second) * ((col + 1) // 2)
    row1 = base[:col]
    row2 = (second + first) * ((col + 1) // 2)
    row2 = row2[:col]

    board = []
    for r in range(row):
        board.append(row1 if r % 2 == 0 else row2)

    return board

board_1 = make_chess(1, row, col)
print("\n".join(board_1))
print('------------')
board_2 = make_chess(2, row, col)
print("\n".join(board_2))
print('------------')

def compare_strings(s1, s2):
    # 두 문자열 중 짧은 길이에 맞춰 비교
    min_len = min(len(s1), len(s2))
    result = ""

    for i in range(min_len):
        if s1[i] == s2[i]:
            result += "0"
        else:
            result += "1"

    return result