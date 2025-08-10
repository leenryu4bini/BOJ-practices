#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11050                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11050                          #+#        #+#      #+#     #
#    Solved: 2025/08/10 12:41:03 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, k= map(int, input().split())
l=[]
i=1
while True:
    l.append(i)
    i+=1
    if i>n: break

from itertools import combinations
result= list(combinations(l,k))
print(len(result))