import math
def find_SoNguyenTo(n):
    if n < 2:
        return []

    primes = 0
    for num in range(2, n + 1):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
            else :
                primes += num
                break

    return primes

if __name__ == "__main__":
    while True:
        try:
            input_n = int(input("Nhập vào một số nguyên dương n: "))
            if input_n > 0:
                primes = (find_SoNguyenTo(input_n))
                print(f"Các số nguyên tố từ 2 đến {input_n} là: {primes}")
                break
            else:
                print("Vui lòng nhập một số nguyên dương.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")