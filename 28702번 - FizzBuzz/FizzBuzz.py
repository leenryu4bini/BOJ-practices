#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28702                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28702                          #+#        #+#      #+#     #
#    Solved: 2025/08/17 19:15:14 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''import numbers

strlst= []
for _ in range(3):
    s= input()
    try:
        s= int(s)
        strlst.append(s)
        continue
    except:
        strlst.append(s)
        continue

type(strlst[2])

for i in range(3,0,-1):
    if isinstance(strlst[i-1],numbers.Number):
        ind= i-1
        plus= 3-ind
        num= strlst[ind]+plus
if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%3==0:
    print('Fizz')
elif num%5==0:
    print('Buzz')
else:
    print(num)'''

strlst= []
for _ in range(3):
    s= input()
    strlst.append(s)

for i in range(3,0,-1):
    if strlst[i-1].isnumeric():
        ind= i-1
        plus= 3-ind
        num= int(strlst[ind])+plus

if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%3==0:
    print('Fizz')
elif num%5==0:
    print('Buzz')
else:
    print(num)