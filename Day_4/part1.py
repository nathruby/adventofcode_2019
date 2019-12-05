INPUT = '146810-612564'

def find_passwords_in_input_range(input):

    input_array = INPUT.split('-')

    start = int(input_array[0])
    end = int(input_array[1])

    password_count = 0

    for password in range(start, end+1):
        if is_password_valid(password):
            password_count+=1

    print(password_count)
    
def is_password_valid(password):

    current_digit = str(password)[:1]
    is_valid = False

    for next_digit in str(password)[1:]:

        if int(next_digit) < int(current_digit):
            return False

        if int(next_digit) == int(current_digit):
            is_valid = True

        current_digit = next_digit

    return is_valid

if __name__ == "__main__":
    find_passwords_in_input_range(INPUT)