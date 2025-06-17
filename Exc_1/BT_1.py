

def convert_String(str_input):
    lst_input = str_input.split(" ")
    lst_output = []
    for i in lst_input:
        i.lower()
        i = i.capitalize()
        lst_output.append(i)
    return ' '.join(lst_output)

a = print(convert_String(str_input = input("Enter a string: ")))