###Palindrome Free Strings
###not done

def palindrome_free(num,test):
    
    max_count = 2 ** test.count('?')
    result = combination([test],max_count)
    print(result)
        
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
    print(c5)
    print(c6)
    count = 0
    for i in result:
        for j in c5:
            if i.find(j) > -1:
                count += 1
                break
        for j in c6:
            if i.find(j) > -1:
                count += 1
                break
    
    if count >= len(result):
        print('impossible')
    else:
        print('possible')
    
def combination(case,max_count):
    temp = []
    for i in case:
        pos = i.find('?')
        temp.append(i[:pos] + '0' + i[pos+1:])
        temp.append(i[:pos] + '1' + i[pos+1:])
    if len(temp) == max_count:
        return temp
    else:
        return combination(temp,max_count)

palindrome_free(9,'100???001')
### impossible
palindrome_free(5,'100??')
### possible
palindrome_free(6,'110??1')
### impossible
palindrome_free(6,'100??1')
### possible
