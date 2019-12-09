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

        while not self.halted:
            
            instruction = self.data[self.pointer]
            op_code = instruction % 100
            modes = instruction // 100

            arg_kinds = OPS[op_code]
            value_1, value_2, value_3, value_4 = self.get_args(arg_kinds, modes)
            self.pointer += 1 + len(arg_kinds)

            if op_code == HALT:
                self.halted = True
                self.op_code_99()

            if op_code == ADD:
                self.op_code_1(value_1, value_2, value_3)

            elif op_code == MULT:
                self.op_code_2(value_1, value_2, value_3)

            elif op_code == IN:
                self.op_code_3(value_1)

            elif op_code == OUT:
                self.op_code_4(value_1)

            elif op_code == JUMP_IF_NOT_ZERO:                
                self.op_code_5(value_1, value_2)

            elif op_code == JUMP_IF_ZERO:
                self.op_code_6(value_1, value_2)

            elif op_code == LESS_THAN:
                self.op_code_7(value_1, value_2, value_3)

            elif op_code == EQUALS:
                self.op_code_8(value_1, value_2, value_3)

            elif op_code == ADD_RELATIVE_BASE:
                self.op_code_9(value_1)

    def op_code_1(self, value_1, value_2, value_3):
        self.data[value_3] = value_1 + value_2

    def op_code_2(self, value_1, value_2, value_3):
        self.data[value_3] = value_1 * value_2

    def op_code_3(self, value_1):

        self.data[value_1] = self.inputs.pop(0)

    def op_code_4(self, value_1):

        self.add_output(value_1)

    def op_code_5(self, value_1, value_2):

        if value_1 != 0:
            self.pointer = value_2

    def op_code_6(self, value_1, value_2):

        if value_1 == 0:
            self.pointer = value_2

    def op_code_7(self, value_1, value_2, value_3):

        if value_1 < value_2:
            self.data[value_3] = 1
        else:
            self.data[value_3] = 0

    def op_code_8(self, value_1, value_2, value_3):

        if value_1 == value_2:
            self.data[value_3] = 1
        else:
            self.data[value_3] = 0

    def op_code_9(self, value_1):

        self.relative_base += value_1

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

    boost_computer_1 = Computer(file_input)
    boost_computer_1.add_input(1)
    boost_computer_1.run_computer()

    print("Part 1:", boost_computer_1.read_output())

    boost_computer_2 = Computer(file_input)
    boost_computer_2.add_input(2)
    boost_computer_2.run_computer()

    print("Part 2:", boost_computer_2.read_output())