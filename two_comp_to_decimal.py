TOTAL_WIDTH = int(input("total bits : "))
FRAC_WIDTH = int(input("bits for fraction : "))

# convert binary(4 bits integer + 8 bits fraction) to decimal
def two_comp_to_decimal(two_comp_num):
    position = 0
    result = 0
    while(position < TOTAL_WIDTH):
        if(two_comp_num[position] == '1') : result += pow(2, (TOTAL_WIDTH - FRAC_WIDTH - 1) - position)
        position = position + 1

    return result 
     
num :int = input("2's complement fixed point (should be negative): ")
one_comp_num :str = ""

for i in range(len(num)):
    if(num[i] == '1'): one_comp_num += '0'
    else: one_comp_num += '1'

two_comp_num_temp = bin(int(one_comp_num, 2) + 1)[2:]
two_comp_num = two_comp_num_temp.rjust(TOTAL_WIDTH,'0')
print("decimal :", two_comp_to_decimal(two_comp_num))