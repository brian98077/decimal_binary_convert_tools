########## author : brian98077 ##########
##########  date : 2024/12/08  ##########

TOTAL_WIDTH = int(input("total bits : "))
FRAC_WIDTH = int(input("bits for fraction : "))

# convert decimal point number to 2's complement
def dec_to_two_comp(decimal_num):
    position = TOTAL_WIDTH - FRAC_WIDTH - 1
    result = "1"
    partial_sub = decimal_num + pow(2, position)
    position -= 1

    while(position >= - FRAC_WIDTH):
        two_power = pow(2, position)
        if(partial_sub >= two_power):
            partial_sub -= two_power
            result += "1"
        else:
            result += "0"
        position -= 1

    return result

input_num = input("decimal (<0) : ")
if(float(input_num) >= 0) : print("ERROR : input should be negative")
else :print(dec_to_two_comp(float(input_num)))