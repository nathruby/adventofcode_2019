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
    same_integer_group = {}
    is_valid = True

    for next_digit in str(password)[1:]:

        if int(next_digit) < int(current_digit):
            return not is_valid

        if int(next_digit) == int(current_digit):
            
            if next_digit in same_integer_group:
                same_integer_group[current_digit] += 1
            else:
                same_integer_group[current_digit] = 2

        current_digit = next_digit

    #No Duplicates
    if len(same_integer_group) < 1:
        return not is_valid

    #adjacent digits are not part of a larger group
    for key in same_integer_group:
        if same_integer_group[key] < 3:
            return is_valid
      
    return not is_valid
            
if __name__ == "__main__":
    find_passwords_in_input_range(INPUT)