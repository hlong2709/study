import random
def bai_1():
    print("Bài 1: In số chia hết cho 3 (1-1000)")
    i = 1
    while i <= 1000:
        if i % 3 == 0:
            print(i)
        i += 1
    print()
def bai_2():
    print("Bài 2: Đổi inches sang cm")
    while True:
        try:
            inches = float(input("Nhập số inches (nhập số âm để dừng): "))
            if inches < 0:
                print("kết thúc chương trình")
                break
            cm = inches * 2.54
            print(f"{inches} inches = {cm:.2f} cm")
        except ValueError:
            print("Nhập số vào !")
def bai_3():
    print("Bài 3: Tìm số nhỏ nhất và lớn nhất")
    numbers = []
    while True:
        user_input = input("Nhập số (enter để dừng): ")
        if user_input == "":
            break
        try:
            num = float(user_input)
            numbers.append (num)
        except ValueError:
            print("Only number bro >:(")
    if len(numbers) > 0:
        print(f"min: {{min(numbers0}}, Max: {max(numbers)}") 
    else:
        print("Danh sách rỗng.")
def bai_4():
    print("Bài 4: TRò chs đoán số từ 1 đến 999")
    secret = random.randint(1, 999)
    print("Máy đã chọn số. Đoán đi ;)")
    while True:
        try:
            guess = int(input("Đoán số: "))
            if guess < secret:
                print("Cao hơn nữa nào")
            elif guess > secret:
                print("thấp lại xíu đi nào")
            else:
                print("Chúc mừng bạn đã đoán không sai")
                break
        except ValueError:
            print("Hãy nhập số nguyên nhé.")

def bai_5():
    print("Bài 5: Đăng nhập với 5 cơ hội")
    attempts = 0
    while attempts < 5:
        u = input("Tên người đăng nhập: ")
        p = input("Mật khẩu:")
        if u == "hunglong" and p == "anhlongdeptraiso1thegioikhaicothesanhvaivoianhlong":
            print("Dạ em chào thượng đế ạ <3")
            return 
        else:
            attempts += 1
            print(f"Sai! Còn {5 - attempts} cơ hội nữa.")
    print("Ngươi là ai!")

def bai_6():
    print("Bài 6: Lấy ký tự giữa")
    text = input("Nhập chuỗi: ")
    length = len(text)
    mid = length // 2
    if length % 2 == 1:
        print(f"Ký tự giữa: {text[mid]}")
    else:
        print(f"Ký tự giữa: {text[mid - 1: mid + 1]}")
def bai_7():
    print("Bài 7: Tạo tự viết tắt (acronym)")
    pharse = input("Nhập cụm từ(VD: Viet Nam): ")
    words = pharse.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    print(f"RESULT: {acronym}")

def main():
    while True:
        print("\n================ MENU ================")
        print("Bài 1: In số chia hết cho 3 (1-1000)")
        print("Bài 2: Đổi inches sang cm")
        print("Bài 3: Tìm số nhỏ nhất và lớn nhất")
        print("Bài 4: TRò chs đoán số từ 1 đến 999")
        print("Bài 5: Đăng nhập với 5 cơ hội")
        print("Bài 6: Lấy ký tự giữa")
        print("Bài 7: Tạo tự viết tắt (acronym)")
        print("0. Thoát chương trình")
        print("Xin lỗi thầy vì đã dùng AI cho cái menu này ạ :((")
        print("======================================")
        
        choice = input("Mời bạn chọn chức năng (0-7): ")

        if choice == "1":
            bai_1()
        elif choice == "2":
            bai_2()
        elif choice == "3":
            bai_3()
        elif choice == "4":
            bai_4()
        elif choice == "5":
            bai_5()
        elif choice == "6":
            bai_6()
        elif choice == "7":
            bai_7()
        elif choice == "0":
            print("Gụt Bai!")
            break
        else:
            print("Lựa chọn không đúng, Hãy nhập lại.")
if __name__ == "__main__":
    main()













        