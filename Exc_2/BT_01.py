import math
def tim_so_chinh_phuong(a: int, b: int):
    """
    Hàm kiểm tra xem có số chính phương nào trong khoảng từ a đến b hay không.
    Trả về True nếu có, False nếu không.
    """
    str_output = ""
    for i in range(a, b + 1):
        if i % 3 == 0 and math.sqrt(i).is_integer() == False:
            str_output += (str(i) + ",")
            
    return str_output

if __name__=="__main__":
    
    while True:
 
        input_A = (input("Nhập vào một số A: "))
        input_B = (input("Nhập vào một số B: "))
        
        if input_A.isnumeric() and input_B.isdigit() and int(input_A) < int(input_B):
            print("Các số chính phương trong khoảng từ", input_A, "đến", input_B, "là:" + str(tim_so_chinh_phuong(int(input_A), int(input_B))))
            break
        else:
            print("Vui lòng nhập một số hợp lệ và đảm bảo số đầu tiên lớn hơn số thứ hai.")
    