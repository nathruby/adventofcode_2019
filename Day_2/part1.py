INPUT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0]

def run_computer(codes):

    codes[1] = 12
    codes[2] = 2
    i = 0
    
    while i < len(codes): 
        if codes[i] == 1:
            codes[codes[i+3]] = op_code_1(codes, codes[codes[i+1]], codes[codes[i+2]])
            i+=4

        if codes[i] == 2:
            codes[codes[i+3]] = op_code_2(codes, codes[codes[i+1]], codes[codes[i+2]])
            i+=4

        if codes[i] == 99:
            op_code_99(codes)

def op_code_1(codes, first_digit, second_digit):

    return first_digit + second_digit

def op_code_2(codes, first_digit, second_digit):

    return first_digit * second_digit

def op_code_99(codes):

    print(codes[0])
    quit()

if __name__ == "__main__":
    run_computer(INPUT)