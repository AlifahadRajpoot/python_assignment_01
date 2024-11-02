#  Print all prime numbers between 1 and 50.

lower = 1
upper = 50
for num in range(lower,upper+1):  #yaha par ya lower sa start ho ga or  upper tak chalne wala loop hai

    if num > 1:                   #yaha if tab chala gi jab  num 1 se bada ho ga

        for  i in range(2,num):   #yaha par 2 sa loop  chalne wala hai jiski value num tak chalne wali hai or ya 2 har bar num sa divide ho ga agar ais ka reminder 0 a gya to ya prime number ni ho ga but  agar reminder 0 ni a gya to ya num prime number hai or asa he ya sar number 1 sa 50 tak num par divide hoga
            if num % i == 0:
                break
        else:
            print(num)
