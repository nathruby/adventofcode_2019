POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_NOT_ZERO = 5
JUMP_IF_ZERO = 6
LESS_THAN = 7
EQUALS = 8
ADD_RELATIVE_BASE = 9
HALT = 99

READ = 0
WRITE = 1

#Dictionary of permissions each value has per operation
OPS = {
    ADD: (READ, READ, WRITE),
    MULT: (READ, READ, WRITE),
    INPUT: (WRITE,),
    OUTPUT: (READ,),
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

            if op_code == ADD:
                self.data[value_3] = value_1 + value_2

            elif op_code == MULT:
                self.data[value_3] = value_1 * value_2

            elif op_code == INPUT:
                self.data[value_1] = self.inputs.pop(0)

            elif op_code == OUTPUT:
                self.add_output(value_1)

            elif op_code == JUMP_IF_NOT_ZERO:                
                self.pointer = value_2 if value_1 != 0 else self.pointer

            elif op_code == JUMP_IF_ZERO:
                self.pointer = value_2 if value_1 == 0 else self.pointer

            elif op_code == LESS_THAN:
                self.data[value_3] = 1 if value_1 < value_2 else 0

            elif op_code == EQUALS:
                self.data[value_3] = 1 if value_1 == value_2 else 0

            elif op_code == ADD_RELATIVE_BASE:
                self.relative_base += value_1

    def add_input(self, input):
        self.inputs.append(input)

    def add_output(self, output):
        self.outputs.append(output)

    def read_output(self):
        return self.outputs.pop(0)

    def get_args(self, arg_kinds, modes):
        args = [None] * 4

        for i, kind in enumerate(arg_kinds):
            data_reference_pointer = self.data[self.pointer + 1 + i]
            mode = modes % 10
            modes //= 10

            if mode == RELATIVE:
                data_reference_pointer += self.relative_base

            if mode in (POSITION, RELATIVE):
                self.resize_memory(data_reference_pointer)

                #if data_reference_pointer references a negative address, throw an exception
                #if data_reference_pointer references an address outside current memory, add enough memory
                #so it can reference it and fill with 0s
                if data_reference_pointer < 0:
                    raise Exception(f"Invalid access to negative memory index: {data_reference_pointer}")
                elif data_reference_pointer >= len(self.data):
                    self.data += [0] * (data_reference_pointer + 1 - len(self.data))

                if kind == READ:
                    data_reference_pointer = self.data[data_reference_pointer]
                elif kind != WRITE:
                    raise Exception(f"Invalid arg kind: {kind}")

            elif mode == IMMEDIATE:
                if kind == WRITE:
                    raise Exception(f"Invalid arg mode for write arg: {mode}")
            else:
                raise Exception(f"Invalid arg mode: {mode}")

            args[i] = data_reference_pointer

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