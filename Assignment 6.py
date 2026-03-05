#1
numbers = []
while True:
    user_input = input("Nhập một số nguyên dương (hoặc nhấn Enter để dừng): ")
    if user_input == "":
        break
    numbers.append(float(user_input))
    
numbers.sort(reverse=True)

print("Năm số lớn nhất là:")
print(numbers[:5])

#2
ss = ("Mùa đông", "Mùa xuân", "Mùa hè", "Mùa thu")
month = int(input("Nhập tháng (1-12): "))

if month in [12, 1, 2]:
    print("Tháng", month, "thuộc", ss[0])
elif month in [3, 4, 5]:
    print("Tháng", month, "thuộc", ss[1])
elif month in [6, 7, 8]:
    print("Tháng", month, "thuộc", ss[2])
elif month in [9, 10, 11]:
    print("Tháng", month, "thuộc", ss[3])

#3
names = set()
while True:
    name = input("Nhập tên (hoặc Enter để dừng): ")
    name = name.lower()
    if name =="":
        break
    if name in names:
        print("Tên đã tồn tại, nhập tên khác.")
    else:
        names.add(name)
print("Danh sách tên đã nhập:")
for name in names:
    print(name)

#4
def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?";()')
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

text = "car bike apple banana car bike phone supra"
print(word_frequency(text))

#5
def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
return_list = remove_odds(list)

print(list)
print(return_list)

#6
import random
def estimate_pi():
    N = int(input("Nhập số lần thử: "))
    n = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            n += 1

    pi_estimate = (n / N) * 4
    print("Ước lượng giá trị của π là:", pi_estimate)
estimate_pi()