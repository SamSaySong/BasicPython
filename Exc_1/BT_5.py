
def is_valid_number(input_string: str):
    lst_number = []
    lst_char = []
    for char in input_string:
        if char.isdigit():
            lst_number.append(char)
        else: lst_char.append(char)
            
    return lst_number, lst_char

if __name__=="__main__":
    input_string = input("Enter a string: ")
    lst_number, lst_char = is_valid_number(input_string)
    print(f"List of numbers: {lst_number}")