###challenge_nine

def challenge_nine(case):
    c_str = str(case)
    c_num = int(case)
    add_num = 9 - (c_num % 9)
    new_num = []
    for i in range(len(c_str)+1):
        new_num.append(int(c_str[:i] + str(add_num) + c_str[i:]))
    print(min(new_num))
    
challenge_nine(5)
### 45
challenge_nine(33)
### 333
challenge_nine(12121)
### 121212
challenge_nine(3952)
### 38952
