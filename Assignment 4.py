#1
def check_course_code(code):
    if len(code) != 6:
        return False
    letters = code[:3]
    digits = code[3:]

    if not (letters.isalpha() and letters.isupper()):
        return False
    if not digits.isdigit():
        return False
    return True
#2
def hexadecimal(color):
    if len(color) != 7 or color[0] != '#':
        return False
    a = "0123456789abcdefABCDEF"
    for i in color[1:]:
        if i not in a:
            return False
    return True
#3
def sum_all_numbers(numbers):
    total = 0
    current_num = ""
    for i in numbers:
        if i.isdigit():
            current_num += i
        else:
            if current_num:
                total += int(current_num)
                current_num = ""
    if current_num != "":
        total += int(current_num)
    return total
#4
def hide_phone_numbers(text):
    words = text.split()
    result = []
    for word in words:
        clean_word = word.strip(".,!?;:()[]{}\"'")
        vnnumber = clean_word.startswith("+84")
        ten_digits = len(clean_word) == 10 and clean_word.isdigit()
        if vnnumber or ten_digits:
            redacted = word.replace(clean_word, "[REDACTED]")
            result.append(redacted)
        else:
            result.append(word)
    return " ".join(result)