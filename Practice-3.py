###challenge_nine

def challenge_nine(num):
    num_str = str(num)
    total = 0
    for i in num_str:
        total += int(i)
    if total >= 9:
        return
        
    min_val = 999999999
    diff = 9 - total
    for i in range(len(num_str)+1):
        new_val = int(num_str[:i] + str(diff) + num_str[i:])
        if new_val < min_val:
            min_val = new_val
    print('min: ' + str(min_val))

challenge_nine(5)
### min: 45
challenge_nine(33)
### min: 333
challenge_nine(12121)
### min: 121212
