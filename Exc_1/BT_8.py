
# Viết chương trình đổi chữ xen kẻ 1 chữ hoa và 1 chữ thường. Ví dụ: nhập ABCDEfgh đổi thành AbCdEfGh

def convert_string_case(string: str):
    result = []
    for i, char in enumerate(string):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)



if __name__=="__main__":
    # input_string = input("Enter a string: ")
    input_string = "ABCDEfgh"
    
    output_string = convert_string_case(input_string)
    print(output_string)