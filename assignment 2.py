
import math


# 1) Kiểm tra chiều dài cá zander
def check_zander_length():
    """
    Yêu cầu nhập chiều dài (cm). Nếu < 42 cm thì báo phải thả cá và cho biết
    ngắn hơn giới hạn bao nhiêu cm.
    """
    try:
        length = float(input("Nhập chiều dài cá zander (cm): ").strip())
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập một số.")
        return

    min_size = 42.0
    if length < min_size:
        diff = min_size - length
        print(f"Thả cá về hồ. Cá ngắn hơn giới hạn {min_size} cm là {diff:.1f} cm.")
    else:
        print(f"Cá đạt kích thước tối thiểu ({min_size} cm). Có thể giữ lại.")


# 2) Mô tả loại cabin (sử dụng if/elif/else)
def describe_cabin():
    """
    Yêu cầu nhập loại cabin và in mô tả tương ứng.
    Các loại hợp lệ: LUX, A, B, C (không phân biệt hoa thường).
    """
    cabin = input("Nhập loại cabin (LUX, A, B, C): ").strip().upper()

    if cabin == "LUX":
        print("LUX: cabin trên boong trên có ban công.")
    elif cabin == "A":
        print("A: trên boong để xe, có cửa sổ.")
    elif cabin == "B":
        print("B: cabin không có cửa sổ, nằm trên boong để xe.")
    elif cabin == "C":
        print("C: cabin không có cửa sổ, nằm dưới boong để xe.")
    else:
        print("Invalid cabin class")


# 3) Trạng thái hemoglobin theo giới tính sinh học
def hemoglobin_status():
    """
    Yêu cầu nhập giới tính sinh học và giá trị hemoglobin (g/l),
    rồi in ra là thấp, bình thường hay cao theo khoảng:
      - Nữ (adult females) bình thường: 117 - 155 g/l
      - Nam (adult males) bình thường: 134 - 167 g/l

    Chấp nhận 'male'/'m'/'nam' cho nam, 'female'/'f'/'nu'/'nữ' cho nữ.
    """
    sex = input("Nhập giới tính sinh học (male/female hoặc m/f hoặc nam/nu): ").strip().lower()
    try:
        hb = float(input("Nhập giá trị hemoglobin (g/l): ").strip())
    except ValueError:
        print("Giá trị hemoglobin không hợp lệ. Vui lòng nhập một số.")
        return

    if sex in ("female", "f", "nu", "nữ"):
        low, high = 117.0, 155.0
        sex_label = "Nữ"
    elif sex in ("male", "m", "nam"):
        low, high = 134.0, 167.0
        sex_label = "Nam"
    else:
        print("Giới tính không hợp lệ. Hãy dùng 'male'/'female' hoặc 'm'/'f' hoặc 'nam'/'nu'.")
        return

    if hb < low:
        print(f"Hemoglobin {hb:.1f} g/l: THẤP (phạm vi bình thường cho {sex_label}: {low}-{high} g/l).")
    elif hb > high:
        print(f"Hemoglobin {hb:.1f} g/l: CAO (phạm vi bình thường cho {sex_label}: {low}-{high} g/l).")
    else:
        print(f"Hemoglobin {hb:.1f} g/l: BÌNH THƯỜNG (phạm vi bình thường cho {sex_label}: {low}-{high} g/l).")


# 4) Kiểm tra năm nhuận
def is_leap_year(year: int) -> bool:
    """
    Trả về True nếu là năm nhuận, False nếu không.
    Quy tắc: chia hết cho 4 là nhuận, nhưng nếu chia hết cho 100 thì chỉ là nhuận khi cũng chia hết cho 400.
    """
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


def ask_leap_year():
    """
    Yêu cầu nhập năm và in ra có phải năm nhuận hay không.
    """
    try:
        year = int(input("Nhập năm (ví dụ 2024): ").strip())
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập một năm (số nguyên).")
        return

    if is_leap_year(year):
        print(f"{year} là năm nhuận.")
    else:
        print(f"{year} không phải năm nhuận.")


# 5) Giá pizza theo đơn vị diện tích (USD/m^2) và so sánh
def pizza_unit_price(diameter_cm: float, price_usd: float) -> float:
    """
    Tính và trả về giá tiền theo USD trên mỗi mét vuông cho pizza tròn.
    diameter_cm: đường kính tính bằng cm
    price_usd: giá tính bằng USD

    Diện tích (m^2) = pi * (radius_in_meters)^2
    radius_in_meters = (diameter_cm / 2) / 100
    """
    if diameter_cm <= 0 or price_usd < 0:
        raise ValueError("Đường kính phải > 0 và giá phải >= 0.")
    radius_m = (diameter_cm / 2) / 100.0
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price_usd / area_m2
    return unit_price


def compare_two_pizzas():
    """
    Yêu cầu nhập đường kính và giá của hai pizza, tính giá trên m^2,
    và thông báo pizza nào có giá trị tốt hơn (giá/đơn vị nhỏ hơn).
    """
    try:
        d1 = float(input("Nhập đường kính pizza 1 (cm): ").strip())
        p1 = float(input("Nhập giá pizza 1 (USD): ").strip())
        d2 = float(input("Nhập đường kính pizza 2 (cm): ").strip())
        p2 = float(input("Nhập giá pizza 2 (USD): ").strip())
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập các giá trị số.")
        return

    try:
        up1 = pizza_unit_price(d1, p1)
        up2 = pizza_unit_price(d2, p2)
    except ValueError as e:
        print("Lỗi:", e)
        return

    print(f"Pizza 1: đường kính {d1} cm, giá ${p1:.2f} -> ${up1:.2f} trên m^2")
    print(f"Pizza 2: đường kính {d2} cm, giá ${p2:.2f} -> ${up2:.2f} trên m^2")

    if abs(up1 - up2) < 1e-9:
        print("Hai pizza có cùng giá trên mỗi m^2.")
    elif up1 < up2:
        print("Pizza 1 có giá trị tốt hơn (giá/đơn vị rẻ hơn).")
    else:
        print("Pizza 2 có giá trị tốt hơn (giá/đơn vị rẻ hơn).")


# Menu đơn giản để chạy từng chức năng
def main_menu():
    actions = {
        "1": ("Kiểm tra chiều dài cá zander", check_zander_length),
        "2": ("Mô tả loại cabin", describe_cabin),
        "3": ("Trạng thái hemoglobin", hemoglobin_status),
        "4": ("Kiểm tra năm nhuận", ask_leap_year),
        "5": ("So sánh hai pizza", compare_two_pizzas),
        "q": ("Thoát", None),
    }

    while True:
        print("\nChọn hành động:")
        for key, (desc, _) in actions.items():
            print(f"  {key}: {desc}")
        choice = input("Nhập lựa chọn: ").strip().lower()
        if choice == "q":
            print("Kết thúc chương trình.")
            break
        action = actions.get(choice)
        if action:
            func = action[1]
            func()
        else:
            print("Lựa chọn không hợp lệ. Thử lại.")


if __name__ == "__main__":
    main_menu()