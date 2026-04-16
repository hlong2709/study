#1
def count(File):
    count = 0
    try:
        with open(File, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    count += 1
        return count
    except FileNotFoundError:
        print("Lỗi không tìm thấy file")

File_name = 'kumalala.txt'
result = count(File_name)
print(result)


#2
def fine_key_word(file, keyword):
    line_numbers = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line_num, line_content in enumerate(f, start=1):
                if keyword in line_content:
                    line_numbers.append(line_num)
        return line_numbers
    
    except FileNotFoundError: 
        print("Lỗi không tìm thấy file")

file_name = 'File_mau.txt'
keyword = input("Nhập từ khóa cần tìm vào đây:")

result = fine_key_word(file_name, keyword)
print(result)

#3
def uppercase (file):
    try:
        with open(file, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
        upper_content = content.upper()
        with open('output.txt', 'w', encoding='utf-8') as f_out:
            f_out.write(upper_content)
            print("Đã hoàn thành")

    except FileNotFoundError:
        print("Lỗi không tìm thấy file")

file_name = 'kumalala.txt'
result = uppercase(file_name)

#4
def calculate_avg_score(file):
    total_score = 0
    student_count = 0
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')

                if len(parts) == 2:
                    score = float(parts[1])

                    total_score += score
                    student_count += 1

        if student_count > 0:
            avg = total_score / student_count
            return avg
        else:
            return 0
        
    except FileNotFoundError:
        print("Lỗi không tìm thấy file")

result = calculate_avg_score('kumalala.txt')
print(result)