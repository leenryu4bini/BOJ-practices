#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2609                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2609                           #+#        #+#      #+#     #
#    Solved: 2025/07/27 20:29:36 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m= map(int, input().split())

#최대공약수의 정의..
    #일단 소인수분해 하기, 공통적인 거 찾기

#최소공배수의 정의..
    #소인수분해 해서 공통적인 거

def soinsoo(n):
    i=2
    insoolst=[]
    insoolst_n=[]
    while True:
        if n%i ==0:
            insoolst.append(i)
            n= n//i
        else: i+=1
        if n==1: #몫이 1이 되면 끝내라
            insoolst.append(n)
            break
    for z in list(set(insoolst)):
        z_insoolst= [x for x in insoolst if x==z]
        for k in range(len(z_insoolst)):
            insoolst_n.append(str(z_insoolst[k])+' '+str(k+1))
            insoolst_n= list(set(insoolst_n))
    
    return insoolst_n


#print(soinsoo(int(input())))

n_so= soinsoo(n)
m_so= soinsoo(m)

#print(n_so)
#print(m_so)
comm_f= list(set(n_so) & set(m_so)) #중복을 제거해버린다는 문제!
#print(comm_f)

comm_f2= []
for i in comm_f:
    comm_f2.append(int(i[0]))

#print(comm_f2)

import math
maxf= math.prod(comm_f2)
#print(maxf)

a= int(n/maxf)
b= int(m/maxf)
minm= maxf*a*b

print(maxf)
print(minm)