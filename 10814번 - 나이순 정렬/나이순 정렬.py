#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10814                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10814                          #+#        #+#      #+#     #
#    Solved: 2025/08/10 12:52:44 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n= int(input())
l= [] # 사람 담을 리스트
for i in range(1,n+1):
    age, name= input().split()
    age= int(age)
    l.append([i,age,name])

def age(lst):
    return(lst[1])

l.sort(key=age) # 나이순 정렬.. 어차피 지금 들어온 순서대로니까 상관없지 않을까?

#print(l)

for k in l:
    print(f'{k[1]} {k[2]}')

'''
=== 보너스: 나이가 같을 때 이름 길이 순으로 ===
n= int(input())
l= [] # 사람 담을 리스트
for i in range(1,n+1):
    age, name= input().split()
    l.append([age,name])

def namelen(lst):
    return(len(lst[1]))

def age(lst):
    return(lst[0])

l.sort(key=namelen) 
l.sort(key=age) # 나이순 정렬.. 어차피 지금 들어온 순서대로니까 상관없지 않을까?

print(l)

for k in l:
    print(f'{k[0]} {k[1]}')'''