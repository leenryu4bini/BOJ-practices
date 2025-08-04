#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2231                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2231                           #+#        #+#      #+#     #
#    Solved: 2025/07/27 15:48:12 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

M= int(input())
breaker= False
for a in range(10):
    if breaker== True:
        break
    for b in range(10):
        if breaker== True:
            break
        for c in range(10):
            if breaker== True:
                break        
            for d in range(10):
                if breaker== True:
                    break                  
                for e in range(10):
                    if breaker== True:
                        break  
                    for f in range(10):
                        if 100001*a+10001*b+1001*c+101*d+11*e+2*f== M:
                            breaker= True
                            print(100000*a+10000*b+1000*c+100*d+10*e+f)
                            break
                        else: continue
if breaker== False:
    print(0)