
def convert_to_uppercase(string :str):
    return string.title()


if __name__=="__main__":
    input_string = input("Enter a string: ")
    output_str = convert_to_uppercase(input_string)
    print(output_str)