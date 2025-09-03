#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2025/08/17 20:28:38 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

'''
=== 1차 시도 ===

n1= int(input())
nlst=list(map(int, input().split()))
n2= int(input())
iptlst=map(int, input().split())

for i in iptlst:
    if i in nlst:
        print(1)
    else: print(0)'''

n1= int(input())
nlst=set(map(int, input().split()))
n2= int(input())
iptlst=list(map(int, input().split()))

for i in iptlst:
    if i in nlst:
        print(1)
    else: print(0)