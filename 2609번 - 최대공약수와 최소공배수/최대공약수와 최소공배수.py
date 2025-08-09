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

#n, m= map(int, input().split())

#최대공약수의 정의..
    #일단 소인수분해 하기, 공통적인 거 찾기

#최소공배수의 정의..
    #소인수분해 해서 공통적인 거

'''
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
'''

#다시 시도
# 두 수를 a, b라고 했을 때, 세 가지 경우가 있다고 생각
# (1): 24 12 처럼 a, b 중 하나가 다른 하나의 약수
# (2): 8 6 처럼 a, b가 a, b, 1이 아닌 공통 약수를 가짐 
# __ (이때, 작은 애의 약수 중 8에서 나눴을 때 딱 나누어 떨어지는 거 중에 가장 큰 거 만들면 됨.)
# (3): 3 7 처럼 공통 약수로 오직 1만 갖는 경우(1, 2 경우가 아니면 최대 공약수가 1인 것으로 진행할 생각)

# 최대공약수가 구해지면, 최소공배수는 최대공약수 * (a/최대공약수) * (b/최대공약수)


import sys
input = sys.stdin.readline

a, b= map(int, input().split())

def factor(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist.append(i)
            flist.append(n//i)
    flist= list(set(flist)) # 중복 제거
    return flist

def maxfact(n, m):
    a= min(n,m) # 작은 애
    b= max(n,m) # 큰 애
    if b%a==0:
        maxf= a
    else:
        flist= factor(a)
        flist.sort(reverse=True)
        can= False
        for f in flist:
            if b%f==0:
                maxf=f
                can= True
                break
            else: continue
        if not can:
            maxf= 1
    return maxf

mf= maxfact(a, b)
mma= a//mf
mmb= b//mf
mm= mf*mma*mmb # 최소공배수= 최대공약수 곱하기 각각의 몫

print(mf)
print(mm)