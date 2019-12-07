import copy
import itertools

class HaltException(Exception):
    pass

def get_input():
    input = []

    with open('input.txt', 'r') as orbit_plan:
        for line in orbit_plan:
            input = [ int(i) for i in line.split(',')]
    
    return input


def run_computer(codes, inputs):

    i = 0
    output = 0

    while i < len(codes):
        op_code = int(str(codes[i])[-2:])

        if op_code == 99:
            op_code_99()

        instruction_mode_1 = str(codes[i])[-3:-2] if str(codes[i])[-3:-2] else 0
        instruction_mode_2 = str(codes[i])[-4:-3] if str(codes[i])[-4:-3] else 0
        #instruction_mode_3 = str(codes[i])[-5:-4] if str(codes[i])[-5:-4] else 0

        parameter_1 = codes[i+1] if instruction_mode_1 == '1' else codes[codes[i+1]]

        if op_code == 1:
            
            parameter_2 = codes[i+2] if instruction_mode_2 == '1' else codes[codes[i+2]]
            parameter_3 = codes[i+3]

            op_code_1(codes, parameter_1, parameter_2, parameter_3)
            i+=4

        elif op_code == 2:
                
            parameter_2 = codes[i+2] if instruction_mode_2 == '1' else codes[codes[i+2]]
            parameter_3 = codes[i+3]

            op_code_2(codes, parameter_1, parameter_2, parameter_3)
            i+=4

        elif op_code == 3:

            parameter_1 = codes[i+1]
            input = inputs.pop(0)

            op_code_3(codes, input, parameter_1)
            i+=2

        elif op_code == 4:

            return op_code_4(codes, parameter_1)

        elif op_code == 5:
            
            parameter_2 = codes[i+2] if instruction_mode_2 == '1' else codes[codes[i+2]]
            
            i = parameter_2 if op_code_5(parameter_1, parameter_2) else i+3

        elif op_code == 6:

            parameter_2 = codes[i+2] if instruction_mode_2 == '1' else codes[codes[i+2]]

            i = parameter_2 if op_code_6(parameter_1, parameter_2) else i+3

        elif op_code == 7:

            parameter_2 = codes[i+2] if instruction_mode_2 == '1' else codes[codes[i+2]]
            parameter_3 = codes[i+3]

            op_code_7(codes, parameter_1, parameter_2, parameter_3)
            i+=4

        elif op_code == 8:

            parameter_2 = codes[i+2] if instruction_mode_2 == '1' else codes[codes[i+2]]
            parameter_3 = codes[i+3]

            op_code_8(codes, parameter_1, parameter_2, parameter_3)
            i+=4

    return output

def op_code_1(codes, value_1, value_2, value_3):

    codes[value_3] = value_1 + value_2

def op_code_2(codes, value_1, value_2, value_3):

    codes[value_3] = value_1 * value_2

def op_code_3(codes, mode, value_1):

    codes[value_1] = mode

def op_code_4(codes, value_1):

    return value_1

def op_code_5(value_1, value_2):

    if value_1 != 0:
        return True

    return False

def op_code_6(value_1, value_2):

    if value_1 == 0:
        return True
    
    return False

def op_code_7(codes, value_1, value_2, value_3):

    if value_1 < value_2:
        codes[value_3] = 1
    else:
        codes[value_3] = 0

def op_code_8(codes, value_1, value_2, value_3):

    if value_1 == value_2:
        codes[value_3] = 1
    else:
        codes[value_3] = 0

def op_code_99():
    raise HaltException()

if __name__ == "__main__":
    original_input = get_input()
    best_mode = ()
    max_output = -99999999

    for mode_sequence in itertools.permutations(range(5)):

        amps = []
        output = 0
        
        for i in range(len(mode_sequence)):
            
            mode_inputs = [mode_sequence[i], output]
            data_input = copy.deepcopy(original_input)
            output = run_computer(data_input, mode_inputs)

        if output > max_output:
            best_mode = mode_sequence
            max_output = output


    print(max_output, best_mode)