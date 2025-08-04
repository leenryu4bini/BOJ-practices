#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2798                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2798                           #+#        #+#      #+#     #
#    Solved: 2025/07/27 19:22:56 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations

n, M= map(int,input().split())
numlst= list(map(int,input().split()))
numlst.sort()
#print(numlst)

comb= list(combinations(numlst,3))

sumlst= []

for i in comb:
    sumlst.append(sum(i))

sumlst.sort(reverse=True)
#print(sumlst)

sumlst= [x for x in sumlst if x<= M]
#print(sumlst)
print(sumlst[0])