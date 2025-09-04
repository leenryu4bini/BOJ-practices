#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15829                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15829                          #+#        #+#      #+#     #
#    Solved: 2025/09/03 21:44:39 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

## \[H = \sum_{i=0}^{l-1}{a_ir^i} \mod M\]
## r을 31
## M을 1234567891

L= int(input())
strng= input()
strlst=[]
strlst2=[]
r= 31
m= 1234567891

mapdict={'a':1, 'b':2, 'c':3, 'd':4, 'e': 5, 'f':6, 
         'g': 7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12,
          'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18,
           's':19, 't':20, 'u':21, 'v':22, 'w': 23, 'x':24,
            'y':25, 'z':26 }


for i in strng:
    strlst.append(i)

for i, v in enumerate(strlst): # enumerate 사용해서 인덱스, 
    strlst[i] = mapdict.get(v) # 값을 받아오기

for j in range(L):
    alph= strlst[j]
    fin= alph*(r**j)
    strlst2.append(fin)

s= sum(strlst2)
print(s%m)