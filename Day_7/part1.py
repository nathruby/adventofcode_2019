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

class Computer():
    def __init__(self, data):

        self.data = data.copy()
        self.pointer = 0
        self.halted = False
        self.inputs = []
        self.output = 0

    def run_computer(self):

        while self.pointer < len(self.data):
            op_code = int(str(self.data[self.pointer])[-2:])

            if op_code == 99:
                self.op_code_99()

            instruction_mode_1 = str(self.data[self.pointer])[-3:-2] if str(self.data[self.pointer])[-3:-2] else 0
            instruction_mode_2 = str(self.data[self.pointer])[-4:-3] if str(self.data[self.pointer])[-4:-3] else 0
            #instruction_mode_3 = str(codes[i])[-5:-4] if str(codes[i])[-5:-4] else 0

            parameter_1 = self.data[self.pointer+1] if instruction_mode_1 == '1' else self.data[self.data[self.pointer+1]]

            if op_code == 1:
                
                parameter_2 = self.data[self.pointer+2] if instruction_mode_2 == '1' else self.data[self.data[self.pointer+2]]
                parameter_3 = self.data[self.pointer+3]

                self.op_code_1(parameter_1, parameter_2, parameter_3)

            elif op_code == 2:
                    
                parameter_2 = self.data[self.pointer+2] if instruction_mode_2 == '1' else self.data[self.data[self.pointer+2]]
                parameter_3 = self.data[self.pointer+3]

                self.op_code_2(parameter_1, parameter_2, parameter_3)

            elif op_code == 3:

                parameter_1 = self.data[self.pointer+1]
                input = self.inputs.pop(0)

                self.op_code_3(input, parameter_1)

            elif op_code == 4:

                return self.op_code_4(parameter_1)

            elif op_code == 5:
                
                parameter_2 = self.data[self.pointer+2] if instruction_mode_2 == '1' else self.data[self.data[self.pointer+2]]
                
                self.op_code_5(parameter_1, parameter_2)

            elif op_code == 6:

                parameter_2 = self.data[self.pointer+2] if instruction_mode_2 == '1' else self.data[self.data[self.pointer+2]]

                self.op_code_6(parameter_1, parameter_2)

            elif op_code == 7:

                parameter_2 = self.data[self.pointer+2] if instruction_mode_2 == '1' else self.data[self.data[self.pointer+2]]
                parameter_3 = self.data[self.pointer+3]

                self.op_code_7(parameter_1, parameter_2, parameter_3)

            elif op_code == 8:

                parameter_2 = self.data[self.pointer+2] if instruction_mode_2 == '1' else self.data[self.data[self.pointer+2]]
                parameter_3 = self.data[self.pointer+3]

                self.op_code_8(parameter_1, parameter_2, parameter_3)

        return output

    def op_code_1(self, value_1, value_2, value_3):

        self.data[value_3] = value_1 + value_2
        self.pointer += 4

    def op_code_2(self, value_1, value_2, value_3):

        self.data[value_3] = value_1 * value_2
        self.pointer += 4

    def op_code_3(self, mode, value_1):

        self.data[value_1] = mode
        self.pointer += 2

    def op_code_4(self, value_1):

        self.pointer += 2
        return value_1

    def op_code_5(self, value_1, value_2):

        if value_1 != 0:
            self.pointer = value_2
        else:
            self.pointer += 3

    def op_code_6(self, value_1, value_2):

        if value_1 == 0:
            self.pointer = value_2
        else:
            self.pointer += 3

    def op_code_7(self, value_1, value_2, value_3):

        if value_1 < value_2:
            self.data[value_3] = 1
        else:
            self.data[value_3] = 0
        
        self.pointer += 4

    def op_code_8(self, value_1, value_2, value_3):

        if value_1 == value_2:
            self.data[value_3] = 1
        else:
            self.data[value_3] = 0

        self.pointer += 4

    def op_code_99(self):
        raise HaltException()

    def add_input(self, input):
        self.inputs.append(input)

if __name__ == "__main__":

    file_input = get_input()
    best_mode = ()
    max_output = -99999999

    for mode_sequence in itertools.permutations(range(5)):

        output = 0

        for i in range(len(mode_sequence)):
            
            amp_computer = Computer(file_input)
            amp_computer.add_input(mode_sequence[i])
            amp_computer.add_input(output)
            output = amp_computer.run_computer()

        if output > max_output:
            best_mode = mode_sequence
            max_output = output


    print(max_output, best_mode)