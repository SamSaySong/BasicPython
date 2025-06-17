# Viết chương trình nhập vào một chuỗi ký tự. Kiểm tra xem chuỗi đó có đối xứng không? Chuỗi đối xứng là chuỗi khi viết ngược lại vẫn được như chuỗi ban đầu.
def is_chuoidoixung(string: str) -> bool:
    cleaned_string = ''.join(string.split()).lower()
    
    return cleaned_string == cleaned_string[::-1]


if __name__=="__main__":
    # input_string = input("Enter a string: ")
    input_string = input("Nhập vào một chuỗi ký tự: ")
    if is_chuoidoixung(input_string):
        print(f"Chuỗi '{input_string}' là chuỗi đối xứng.")
    else:
        print(f"Chuỗi '{input_string}' không phải là chuỗi đối xứng.")