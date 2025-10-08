#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1436                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1436                           #+#        #+#      #+#     #
#    Solved: 2025/10/09 01:02:25 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from itertools import permutations

numlst=[]

#4자리
for i in range(10):
    n= ['666',f'{i}']
    for p in permutations(n):
        numlst.append(''.join(p))

numlst= list(set(numlst))
#print(numlst)


#5자리
for i in range(10):
    for j in range(10):
        n= ['666',f'{i}',f'{j}']
        for p in permutations(n):
            numlst.append(''.join(p))

numlst= list(set(numlst))
#print(numlst)

#6자리
for i in range(10):
    for j in range(10):
        for k in range(10):
            n= ['666',f'{i}',f'{j}', f'{k}']
            for p in permutations(n):
                 numlst.append(''.join(p))


numlst= list(set(numlst))
#print(numlst)

#7자리
for i in range(10):
    for j in range(10):
        for k in range(10):
            for r in range(10):
                n = ['666', f'{i}', f'{j}', f'{k}', f'{r}']
                for p in permutations(n):
                    numlst.append(''.join(p))

numlst= list(set(numlst))
#print(numlst)



numlst= list(map(int,numlst))
numlst= list(set(numlst))
numlst.sort()
#print(numlst)

#print(len(numlst))
#print(numlst[N-1])

N= int(input())
print(numlst[N-1])
