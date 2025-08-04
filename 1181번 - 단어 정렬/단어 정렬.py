#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2025/08/04 17:07:04 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

'''n= int(input())
wrdlst= []
for i in range(n):
    a= input()
    wrdlst.append(a)

wrdlst=list(set(wrdlst)) #중복 제거
wrdlst.sort(key=len) #길이 정렬!이렇게 key 함수를 지정해 줄 수 있다! 


#'길이가 같으면 사전 순으로' 적용
#리스트 안에 리스트를 넣어서 하고파..

lstwrdlst= []
samenumlst= []
for w in wrdlst:
    samenumlst.append(w)
    for k in wrdlst:
        if len(k)== len(w):
            samenumlst.append(k)
            samenumlst= list(set(samenumlst))
            samenumlst.sort() #넣을 때 알파벳 순서대로
    if samenumlst in lstwrdlst:
        samenumlst=[] #중복 안 되게 하기
        continue
    lstwrdlst.append(samenumlst)
    samenumlst=[]

#프린트하기
for i in lstwrdlst:
    for k in i:
        print(k)
'''

n= int(input())
wrdlst= []
for i in range(n):
    a= input()
    wrdlst.append(a)

wrdlst=list(set(wrdlst)) #중복 제거
wrdlst.sort(key=len) #길이 정렬!이렇게 key 함수를 지정해 줄 수 있다! 

maxlen= len(wrdlst[-1])

lstwrdlst= []

for i in range(1,maxlen+1):
    samenumlst=[]
    for w in wrdlst:
        if len(w)== i:
            samenumlst.append(w)
            samenumlst= list(set(samenumlst))
    if samenumlst!= []:
        lstwrdlst.append(samenumlst)

#프린트하기
for i in lstwrdlst:
    i.sort() 
    #알파벳 순서대로 정렬
    for k in i:
        print(k)