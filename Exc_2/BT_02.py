import datetime
import random

def get_milliseconds():
    thoi_gian = datetime.datetime.now()
    time_second = thoi_gian.strftime("%f")
    mili_second = time_second[0:3]
    return int(mili_second)

# def dap_an():
#     dap_an = random.randint(dap_an_value, 999)
#     return dap_an


if __name__=="__main__":
    
    x = 1
    dap_an_value = get_milliseconds()
    print("Đáp án chính xác là: " + str(dap_an_value))
    while x < 6:
        
        try:
            mini_game = input("Vui lòng nhập số trong khoảng từ 1 ~ 999: ")
            if len(mini_game) <= 3:
                if int(mini_game) == dap_an_value:
                    print("Bạn đã dự đoán chính xác số: " + str(dap_an_value))
                    break
                elif  int(mini_game) in range(dap_an_value - 10, dap_an_value + 10):
                    print("Bạn đoán gần đúng rồi")
                    x += 1
                else:
                    if x == 5:
                        print("Bạn đã đoán sai 5 lần, kết quả đã thay đổi. Mời bạn đoán lại.")
                        break
                    print(f"Bạn đã trả lời sai {x}, mời bạn đoán lại.")
                    x += 1
            else:
                print("Vui lòng nhập một số có độ dài tối đa là 3 chữ số.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
