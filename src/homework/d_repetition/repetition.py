#for loop
def get_factorial(num):
    if num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)
    
#while loop
def sum_odd_numbers(num):
    sum = 0
    cnt = 1
    while(cnt <= num ):
        sum += cnt
        cnt += 2
    return sum