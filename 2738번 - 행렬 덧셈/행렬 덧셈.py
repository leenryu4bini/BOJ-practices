#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2025/09/04 20:17:01 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m= map(int, input().split())

matr_a_lst= []
for i in range(n):
    matr_a_lst= matr_a_lst+list(map(int, input().split()))

#print(matr_a_lst)

matr_b_lst= []
for i in range(n):
    matr_b_lst= matr_b_lst+list(map(int, input().split()))

#print(matr_b_lst)

matr_sum=[]
for i in range(n*m):
    s= matr_a_lst[i]+matr_b_lst[i]
    matr_sum.append(s)


i=0
while True:
    print(*matr_sum[i:i+m])
    i= i+m
    if i>m*n-1: break