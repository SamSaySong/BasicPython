
def find_last_and_first_name(string: str):
    lst_name = string.split(" ")
    first_name = lst_name[0]
    middle_name = " ".join(lst_name[1:-1])
    last_name = lst_name[-1]
    
    return first_name, middle_name, last_name


if __name__=="__main__":
    input_string = input("Enter a string: ")
    first_name, middle_name, last_name = find_last_and_first_name(input_string)
    print(f"First name: {first_name}, Middle name: {middle_name}, Last name: {last_name}")