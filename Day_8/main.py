HEIGHT = 6
WIDTH = 25

def get_input():
    input = []

    with open('input.txt', 'r') as orbit_plan:
        for line in orbit_plan:
            input = line.strip('\n')
    
    return input

def some_function(input):
    
    input_position = 0
    min_zero_count = 999999
    min_zero_count_layer = -1
    layers = []
    layer_count = 0

    while input_position < len(input):

        layer = []
        layer_zero_count = 0
        for row in range(HEIGHT):

            layer.append([])
            for column in range(WIDTH):

                if int(input[input_position]) == 0:
                    layer_zero_count += 1
                
                layer[row].append(int(input[input_position]))
                input_position += 1

        if layer_zero_count < min_zero_count:
            min_zero_count = layer_zero_count
            min_zero_count_layer = layer_count

        layers.append(layer)
        layer_count += 1

    print( min_zero_count_layer, min_zero_count)

    number_of_ones = 0
    number_of_twos = 0

    for row in layers[min_zero_count_layer]:
        for column in row:

            if column == 1:
                number_of_ones += 1
            if column == 2:
                number_of_twos += 1

    print(number_of_ones * number_of_twos)
    
    #Intialize image
    layer_image = [ row for row in layers[0]]

    for layer in layers:

        for row in range(HEIGHT):

            for column in range(WIDTH):

                if layer_image[row][column] > layer[row][column] and layer_image[row][column] == 2:
                    layer_image[row][column] = layer[row][column]

    for row in layer_image:
        print(row)            
    ################################################



if __name__ == "__main__":

    file_input = get_input()
    some_function(file_input)
