import copy
import itertools

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
        self.outputs = []

    def run_computer(self):

        while self.pointer < len(self.data):

            op_code = int(str(self.data[self.pointer])[-2:])

            if op_code == 99:
                self.op_code_99()
                return

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

                #if no more inputs, move onto next amp
                if self.inputs:
                    parameter_1 = self.data[self.pointer+1]
                    self.op_code_3(parameter_1)
                else:
                    return

            elif op_code == 4:

                self.op_code_4(parameter_1)

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

    def op_code_1(self, value_1, value_2, value_3):

        self.data[value_3] = value_1 + value_2
        self.pointer += 4

    def op_code_2(self, value_1, value_2, value_3):

        self.data[value_3] = value_1 * value_2
        self.pointer += 4

    def op_code_3(self, value_1):

        self.data[value_1] = self.inputs.pop(0)
        self.pointer += 2

    def op_code_4(self, value_1):

        self.add_output(value_1)
        self.pointer += 2

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
        self.halted = True

    def add_input(self, input):
        self.inputs.append(input)

    def add_output(self, output):
        self.outputs.append(output)

    def read_output(self):
        return self.outputs.pop(0)

def part1():
    
    file_input = get_input()
    best_mode = ()
    max_output = -99999999

    for mode_sequence in itertools.permutations(range(5)):
            
        output = 0

        #for each amp, reset input and feed output to be new amp's input
        #beginning with a signal input of 0
        for amp in range(len(mode_sequence)):

            system_computer = Computer(file_input)
            system_computer.add_input(mode_sequence[amp])
            system_computer.add_input(output)
            system_computer.run_computer()

            output = system_computer.read_output()

        if output > max_output:
            best_mode = mode_sequence
            max_output = output


    print("Part 1:", max_output, best_mode)

def part2():

    file_input = get_input()
    best_mode = ()
    max_output = -99999999

    for mode_sequence in itertools.permutations(range(5, 10)):

        amps = []
        for i in range(5):
            amps.append(Computer(file_input))
            amps[i].add_input(mode_sequence[i])
            
        output = 0
        current_amp = 0

        #Keep reading outputs from amps until E(4) is halted, get its last output and stop
        while True:

            amps[current_amp].add_input(output)
            
            amps[current_amp].run_computer()

            output = amps[current_amp].read_output()

            if amps[4].halted:
                break

            #Amp A(0), B(1), C(2), D(3), E(4), A(0)
            current_amp = current_amp + 1 if current_amp < 4 else 0

        if output > max_output:
            best_mode = mode_sequence
            max_output = output


    print("Part 2:", max_output, best_mode)

if __name__ == "__main__":
    part1()
    part2()