user_input = input("Введите свой возраст:")
if user_input.isdigit():
    age = int(user_input)
    print(f"Через 5 лет вам будет {age + 5}")
else:
    print("Ошибка: введено не коректное значени!")