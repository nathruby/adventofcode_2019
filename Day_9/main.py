POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

ADD = 1
MULT = 2
IN = 3
OUT = 4
JUMP_IF_NOT_ZERO = 5
JUMP_IF_ZERO = 6
LESS_THAN = 7
EQUALS = 8
ADD_RELATIVE_BASE = 9
HALT = 99

READ = 0
WRITE = 1

OPS = {
    ADD: (READ, READ, WRITE),
    MULT: (READ, READ, WRITE),
    IN: (WRITE,),
    OUT: (READ,),
    JUMP_IF_NOT_ZERO: (READ, READ),
    JUMP_IF_ZERO: (READ, READ),
    LESS_THAN: (READ, READ, WRITE),
    EQUALS: (READ, READ, WRITE),
    ADD_RELATIVE_BASE: (READ,),
    HALT: (),
}

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
        self.relative_base = 0
        self.halted = False
        self.inputs = []
        self.outputs = []

    def run_computer(self):

        while self.data[self.pointer] != HALT:
            
            op_code = self.data[self.pointer] % 100
            modes = self.data[self.pointer] // 100

            arg_kinds = OPS[op_code]
            a, b, c, d = self.get_args(arg_kinds, modes)
            self.pointer += 1 + len(arg_kinds)
            print(a,b,c,d)
            instruction_mode_1 = modes % 10
            instruction_mode_2 = modes // 10
            #instruction_mode_3 = modes // 100

            if op_code == 99:
                self.op_code_99()
                return
                  
            if instruction_mode_1 == 0:
                
                self.resize_memory( self.data[self.pointer+1])
                parameter_1 = self.data[self.data[self.pointer+1]]

            elif instruction_mode_1 == 1:
                
                self.resize_memory( self.pointer+1)
                parameter_1 = self.data[self.pointer+1]

            elif instruction_mode_1 == 2:

                self.resize_memory( self.relative_base + self.data[self.pointer+1])
                parameter_1 = self.data[self.relative_base + self.data[self.pointer+1]]

            if op_code == ADD:

                parameter_2 = None
                parameter_3 = self.data[self.pointer+3]

                if instruction_mode_2 == 0:

                    self.resize_memory( self.data[self.pointer+2])
                    parameter_2 = self.data[self.data[self.pointer+2]]

                elif instruction_mode_2 == 1:

                    self.resize_memory( self.pointer+2)
                    parameter_2 = self.data[self.pointer+2]

                elif instruction_mode_2 == 2:

                    self.resize_memory( self.relative_base + self.data[self.pointer+2])
                    parameter_1 = self.data[self.relative_base + self.data[self.pointer+2]]

                self.op_code_1(parameter_1, parameter_2, parameter_3)

            elif op_code == MULT:

                parameter_2 = None
                parameter_3 = self.data[self.pointer+3]

                if instruction_mode_2 == 0:

                    self.resize_memory( self.data[self.pointer+2])
                    parameter_2 = self.data[self.data[self.pointer+2]]

                elif instruction_mode_2 == 1:

                    self.resize_memory( self.pointer+2)
                    parameter_2 = self.data[self.pointer+2]

                elif instruction_mode_2 == 2:

                    self.resize_memory( self.relative_base + self.data[self.pointer+2])
                    parameter_1 = self.data[self.relative_base + self.data[self.pointer+2]]

                self.op_code_2(parameter_1, parameter_2, parameter_3)

            elif op_code == IN:

                #if no more inputs, move onto next amp
                if self.inputs:
                    parameter_1 = self.data[self.pointer+1]
                    self.op_code_3(parameter_1)
                else:
                    return

            elif op_code == OUT:

                self.op_code_4(parameter_1)

            elif op_code == JUMP_IF_NOT_ZERO:
                
                parameter_2 = None
                parameter_3 = self.data[self.pointer+3]

                if instruction_mode_2 == 0:

                    self.resize_memory( self.data[self.pointer+2])
                    parameter_2 = self.data[self.data[self.pointer+2]]

                elif instruction_mode_2 == 1:

                    self.resize_memory( self.pointer+2)
                    parameter_2 = self.data[self.pointer+2]

                elif instruction_mode_2 == 2:

                    self.resize_memory( self.relative_base + self.data[self.pointer+2])
                    parameter_1 = self.data[self.relative_base + self.data[self.pointer+2]]
                
                self.op_code_5(parameter_1, parameter_2)

            elif op_code == JUMP_IF_ZERO:

                parameter_2 = None
                parameter_3 = self.data[self.pointer+3]

                if instruction_mode_2 == 0:

                    self.resize_memory( self.data[self.pointer+2])
                    parameter_2 = self.data[self.data[self.pointer+2]]

                elif instruction_mode_2 == 1:

                    self.resize_memory( self.pointer+2)
                    parameter_2 = self.data[self.pointer+2]

                elif instruction_mode_2 == 2:

                    self.resize_memory( self.relative_base + self.data[self.pointer+2])
                    parameter_1 = self.data[self.relative_base + self.data[self.pointer+2]]

                self.op_code_6(parameter_1, parameter_2)

            elif op_code == LESS_THAN:

                parameter_2 = None
                parameter_3 = self.data[self.pointer+3]

                if instruction_mode_2 == 0:

                    self.resize_memory( self.data[self.pointer+2])
                    parameter_2 = self.data[self.data[self.pointer+2]]

                elif instruction_mode_2 == 1:

                    self.resize_memory( self.pointer+2)
                    parameter_2 = self.data[self.pointer+2]

                elif instruction_mode_2 == 2:

                    self.resize_memory( self.relative_base + self.data[self.pointer+2])
                    parameter_1 = self.data[self.relative_base + self.data[self.pointer+2]]

                parameter_3 = self.data[self.pointer+3]

                self.op_code_7(parameter_1, parameter_2, parameter_3)

            elif op_code == EQUALS:

                parameter_2 = None
                parameter_3 = self.data[self.pointer+3]

                if instruction_mode_2 == 0:

                    self.resize_memory( self.data[self.pointer+2])
                    parameter_2 = self.data[self.data[self.pointer+2]]

                elif instruction_mode_2 == 1:

                    self.resize_memory( self.pointer+2)
                    parameter_2 = self.data[self.pointer+2]

                elif instruction_mode_2 == 2:

                    self.resize_memory( self.relative_base + self.data[self.pointer+2])
                    parameter_1 = self.data[self.relative_base + self.data[self.pointer+2]]

                parameter_3 = self.data[self.pointer+3]

                self.op_code_8(parameter_1, parameter_2, parameter_3)

            elif op_code == ADD_RELATIVE_BASE:
                self.op_code_9(parameter_1)

    def op_code_1(self, value_1, value_2, value_3):
        self.resize_memory(value_3)
        self.data[value_3] = value_1 + value_2
        self.pointer += 4

    def op_code_2(self, value_1, value_2, value_3):
        self.resize_memory(value_3)
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
        self.resize_memory(value_3)
        if value_1 < value_2:
            self.data[value_3] = 1
        else:
            self.data[value_3] = 0
        
        self.pointer += 4

    def op_code_8(self, value_1, value_2, value_3):
        self.resize_memory(value_3)
        if value_1 == value_2:
            self.data[value_3] = 1
        else:
            self.data[value_3] = 0

        self.pointer += 4

    def op_code_9(self, value_1):

        self.relative_base += value_1
        self.pointer += 2

    def op_code_99(self):
        self.halted = True

    def add_input(self, input):
        self.inputs.append(input)

    def add_output(self, output):
        self.outputs.append(output)

    def read_output(self):
        return self.outputs.pop(0)

    def get_args(self, arg_kinds, modes):
        args = [None] * 4

        for i, kind in enumerate(arg_kinds):
            data_reference = self.data[self.pointer + 1 + i]
            mode = modes % 10
            modes //= 10

            if mode == RELATIVE:
                data_reference += self.relative_base

            if mode in (POSITION, RELATIVE):
                self.resize_memory(data_reference)

                if data_reference < 0:
                    raise Exception(f"Invalid access to negative memory index: {data_reference}")
                elif data_reference >= len(self.data):
                    self.data += [0] * (data_reference + 1 - len(self.data))

                if kind == READ:
                    data_reference = self.data[data_reference]
                elif kind != WRITE:
                    raise Exception(f"Invalid arg kind: {kind}")

            elif mode == IMMEDIATE:
                if kind == WRITE:
                    raise Exception(f"Invalid arg mode for write arg: {mode}")
            else:
                raise Exception(f"Invalid arg mode: {mode}")

            args[i] = data_reference

        return args

    def resize_memory(self, pointer_index):
        if pointer_index >= len(self.data):
            self.data.extend([0] * (pointer_index + 1 - len(self.data)))
        return
        
if __name__ == "__main__":

    file_input = get_input()

    boost_computer = Computer(file_input)
    boost_computer.run_computer()

    print(boost_computer.read_output())