#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11866                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11866                          #+#        #+#      #+#     #
#    Solved: 2025/08/25 21:50:17 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
n, k= map(int, input().split())

q = deque()
poplst= []

# 1부터 n까지 넣기 (enqueue)
for i in range(1,n+1):
    q.append(i)

# 빼기 (dequeue)
deln = k-1
while True:
# 'rotate' 사용해서 돌면서 deln번째 요소를 제거
    q.rotate(-deln)     # deln번째 요소를 맨 왼쪽으로 돌리기
    x= q.popleft()      # 제거
    poplst.append(x)
    if len(q)==0: break

output = str(poplst).replace('[', '<').replace(']', '>')
print(output)