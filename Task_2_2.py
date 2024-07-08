from collections import deque

def is_palindrome(input_string):
    # Приведення рядка до нижнього регістру та видалення пробілів
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Створення двосторонньої черги
    char_deque = deque(cleaned_string)
    
    # Перевірка на паліндром
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестування функції
test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
]

for test_string in test_strings:
    result = is_palindrome(test_string)
    print(f"'{test_string}' is a palindrome: {result}")
