def total_salary(path: str) -> tuple[int, int]:
    """
    Аналізує текстовий файл із заробітними платами розробників,
    обчислює загальну та середню суму заробітної плати.
    Повертає (0, 0) у разі помилки або відсутності даних.
    """
    total_salary = 0
    num_developers = 0
    
    try:
        # Використання менеджера контексту 'with' та кодування
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                
                # Перевірка формату: очікуємо 2 елементи (ім'я, зарплата)
                if len(parts) == 2:
                    try:
                        # Зарплата – це другий елемент (індекс 1)
                        salary = int(parts[1])
                        total_salary += salary
                        num_developers += 1
                    except ValueError:
                        # Обробка неправильного формату зарплати
                        print(
                            f"Помилка: Неправильний формат заробітної плати '{line.strip()}'"
                        )
                else:
                    # Обробка неправильного формату рядка
                    print(f"Помилка: Неправильний формат даних '{line.strip()}'")
                    
        if num_developers > 0:
            # Використовуємо цілочисельне ділення (//) для отримання int
            average_salary = total_salary // num_developers 
            return total_salary, average_salary
        else:
            print("Помилка: Немає даних про заробітні плати розробників у файлі.")
            return 0, 0
            
    except FileNotFoundError:
        # Обробка відсутності файлу
        print("Помилка: Файл не знайдено.")
        return 0, 0

# Приклад використання функції
# Примітка: використовуйте int() лише для виведення, якщо функція повертає float.
# З цілочисельним діленням int() більше не потрібне у виведенні.
total, average = total_salary("task_1/salary_file.txt")
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
)
