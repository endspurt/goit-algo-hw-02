import queue

# Створити чергу заявок
request_queue = queue.Queue()

# Функція generate_request():
def generate_request():
    # Створити нову заявку
    request = "new_request"
    # Додати заявку до черги
    request_queue.put(request)

# Функція process_request():
def process_request():
    if not request_queue.empty():
        # Видалити заявку з черги
        request = request_queue.get()
        # Обробити заявку
        print(f"Processing {request}")
    else:
        # Вивести повідомлення, що черга пуста
        print("Queue is empty")

# Головний цикл програми:
while True:
    # Поки користувач не вийде з програми:
    user_input = input("Press 'Enter' to generate and process requests or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break
    # Виконати generate_request() для створення нових заявок
    generate_request()
    # Виконати process_request() для обробки заявок
    process_request()

