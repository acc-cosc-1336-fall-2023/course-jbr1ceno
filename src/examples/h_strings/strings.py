def test_config():
    return True

def loop_string_w_while(str):
    indx = 0

    while indx < len(str):
       print(str[indx])
       indx += 1 

def loop_string_w_for(str):
    
    for s_indx in range(0, len(str)):
        #print(s) #shows index
        print(str[s_indx])

def loop_string_w_special_for(str):
    for ch in str:
        print(ch)

def concat_strings(str1, str2):
    return str1 + str2

def slice_string(str):
    return str[6:10]

def slice_w_step_value(str):
    return str[0:len(str):2]


#quiz practice
'''num = 10

def display_num():
    global num
    num = 100
    print(num)
    
num = 0
print(num)'''