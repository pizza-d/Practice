###speed typing

def speed_typing(currect,test):
    max_del = len(test) - len(currect)
    del_count = 0
    currect_inedx = 0
    for i in test:
        if i == currect[currect_inedx]:
            currect_inedx += 1
        else:
            del_count += 1
        if del_count > max_del:
            final = 'impossible'
            break;
        else:
            if currect_inedx == len(currect):
                final = max_del
                break;
    print('delete: ' + str(final))
    
speed_typing('Ilovecoding','IIllovecoding')
### delete: 2
speed_typing('KickstartIsFun','kkickstartiisfun')
### delete: impossible
