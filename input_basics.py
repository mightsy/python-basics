user_input = input ("Введите ваш уровень допуска  1-8:" )
if user_input.isdigit():
    level = int(user_input)
    if 1 <= level <= 6:
       print("Уровень доступа слишком низкий")
    elif level == 8:
       print("Уровень доступа разрешен, вы вошли как Red Team Leader")
    else:
       print("Внимание: неизвестный уровень допуска!")
else:
    print("Ошибка: введено не цифра. Доступ запрещен.")