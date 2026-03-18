#1
numbers = []

print("NHập từng số một, nhấn enter dể thoát.")

while True:
    user_input = input("NHập số: ")
    if user_input == "":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("sai! Vui lòng nhập số hợp lệ.")

if len(numbers) >= 5:
    numbers.sort(reverse=True)
    print("Năm con số lớn nhất (theo thứ tự giảm dần):")
    for num in numbers[:5]:
        print(num)
else:
    print("Chưa nhập đủ só.", len(numbers), "numbers.")


#2
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Nhập một số nguyên: "))

if is_prime(number):
    print(number, "là một số nguyên tố.")
else:
    print(number, "Không phải là số nguyên tố.")


#3
cities = []

print("Nhập vào 5 tên thành phố: ")

for i in range(5):
    city = input(f"City {i + 1}: ")
    cities.append(city)

print("\nThành phố bạn nhập vào:")
for city in cities:
    print(city)


#4
def sum_of_list(numbers):
    return sum(numbers)

# Main program for testing
test_list = [10, 20, 30, 40, 50]
result = sum_of_list(test_list)
print("Danh sách gốc:", test_list)
print("Tổng tất cả các số:", result)


#5
def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]

# Main program for testing
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_odds(test_list)

print("Danh sách gốc: ", test_list)
print("Danh sách bỏ số lẻ: ", filtered_list)