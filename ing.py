import time

def palindrome_free(num,test):
    if len(test) < 5:
        return 'possible(length less than 5)'
        
    
    if num == 5 or num == 6:
        all_c = combination([test])
        for i in all_c:
            if check56(i) == 0:
                print('possible')
                return
        print('impossible')
            
    else:
        rrr = []
        for i in range(num-5):
            t = test[i:i+6]
            v = combination([t])
            no_palin = []
            for j in v:
                if check56(j) == 0:
                    rrr.append(j)
                #     no_palin.append(j)
            
            # if i == 0:
            #     kk = no_palin
            #     continue
            
            # # print(kk)
            # # print(no_palin)
            # # print('\n')
            # zz = []
            # for j in kk:
            #     for l in no_palin:
            #         if j[1:] == l[:-1]:
            #             zz.append(l)
            # #print(zz)
            # if len(zz) == 0:
            #     print('impossible')
            #     return
            # kk = zz
        print(len(rrr))
        print('possible')
    
def combination(case):
    temp = []
    for i in case:
        pos = i.find('?')
        if pos >= 0:
            temp.append(i[:pos] + '0' + i[pos+1:])
            temp.append(i[:pos] + '1' + i[pos+1:])
    # print(len(temp))
    # print(temp)
    if len(temp) == 0:
        return case
    if temp[0].find('?') < 0:
        return temp
    else:
        return combination(temp)
        

def check56(a):
    c5 = []
    c6 = []
    for i in range(2 ** 5):
        x = str(format(i,'b').zfill(5))
        if x == ''.join(reversed(x)):
            c5.append(x)
    for i in range(2 ** 6):
        x = str(format(i,'b').zfill(6))
        if x == x[len(x)::-1]:
            c6.append(x)
            
    for i in c6:
        if a.find(i) >= 0:
            return 1
    for i in c5:
        if a.find(i) >= 0:
            return 1
    return 0

st = time.time()
#palindrome_free(2,'1?')
# palindrome_free(9,'100???001')
# print('---------------------')
# palindrome_free(16,'000101100101100?')# can be 0 or 1
# print('---------------------')
# palindrome_free(17,'000101100101100?1')# can not be 0 or 1
# print('---------------------')
# palindrome_free(18,'000101100101100?01')# only can be 1
# print('---------------------')
# palindrome_free(5,'100??')
# print('---------------------')
# palindrome_free(6,'110??1')
# print('---------------------')
# palindrome_free(6,'100??1')
# print('---------------------')
# palindrome_free(7,'10?00?1')
# print('---------------------')
# palindrome_free(8,'10?0?0?1')
# print('---------------------')
# palindrome_free(25,'1?0??01????????1??0?11??1')
# print('---------------------')
palindrome_free(50000,'?'*50000)# 2818 ok
ed = time.time()
print(ed - st)
