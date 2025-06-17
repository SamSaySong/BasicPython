# Viết chương trình nhập vào số có 3 chữ số. Cho biết dòng chữ mô tả giá trị con số đó. Ví dụ 123 -> một trăm hai mươi ba.

def convert_number_to_words(number: int) -> str:
    

    units_hudred = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["không", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    units = ["không", "một", "hai", "ba", "bốn", "lăm", "sáu", "bảy", "tám", "chín"]

    
    hundred_digit = number // 100
    ten_digit = (number // 10) % 10
    unit_digit = number % 10
    
    result = f"{units_hudred[hundred_digit]} trăm"
    
    if ten_digit > 0:
        result += f" {tens[ten_digit]}"
   
    
    if unit_digit > 0:
        if ten_digit == 0 and hundred_digit > 0:
            result += " lẻ"
        result += f" {units[unit_digit]}"
    
    return result.strip()


if __name__=="__main__":
    
    input_string = input("Nhập vào một số có 3 ký tự: ")
    if input_string.isdigit() and len(input_string) == 3:
        print(convert_number_to_words((int(input_string))))
    else:
        print("Vui lòng nhập một số có 3 chữ số.")