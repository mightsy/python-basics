while True: 
    user_input = input("Введите число:")
    if user_input == "exit":
        print("Выход...")
        break
    try: 
        number = int(user_input)
        if number < 0 or number > 255:
            print("Ошибка: введено не коректное значение!")
        elif number == 127:
            print("Loopback: Вы ввели число 127, это зарезервированный адрес")
        else:
            print("Вы ввели октет коректно")
    except ValueError:
        print("Вы ввели не число!")