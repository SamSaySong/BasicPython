from datetime import *

def count_sundays_on_first_of_month(start: datetime, end : datetime):
    # Nhập ngày bắt đầu và kết thúc theo định dạng dd-mm-yyyy
    count = 0
    year = start.year
    month = start.month

    while year < end.year or (year == end.year and month <= end.month):
        first_day = datetime(year, month, 1)
        print(start)
        print(first_day)
        print(end)
        
        if start <= first_day <= end and first_day.isoweekday() == 7:  
            count += 1

        # Tăng tháng
        month += 1
        if month > 12:
            month = 1
            year += 1
    return count



if __name__ == "__main__":
    while True:
        try:
            start_date = input("Nhập ngày bắt đầu (dd-mm-yyyy): ")
            start = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = input("Nhập ngày kết thúc (dd-mm-yyyy): ")
            end = datetime.strptime(end_date, "%d-%m-%Y")
            print((end - start).days)
            # if  date(end) - date(start) < 0:
            #     print("Ngày kết thúc phải lớn hơn ngày bắt đầu. Vui lòng nhập lại.")
            #     continue
            break
        except ValueError:
            print("Định dạng ngày không hợp lệ. Vui lòng nhập theo định dạng dd-mm-yyyy.")
    
    print("Số Chủ Nhật rơi vào ngày đầu tháng là:", count_sundays_on_first_of_month(start, end))