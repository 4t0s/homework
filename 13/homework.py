def is_valid_knight_move(start, end):
    x1, y1 = start
    x2, y2 = end
    return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)

try:
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    if is_valid_knight_move(start, end):
        print("YES")
    else:
        print("NO")

except ValueError:
    print("Input error")
except :
    print("Произошла ошибка")


"""
Функция plus_two() выполняет одну простую задачу — выводит результат сложения
переданного в нее числа 2 и значения переменной number. В переменную number должно быть
передано число. Обработайте ситуацию, если в эту переменную переданы данные какого-то
другого типа. В случае ошибки напечатайте в консоли сообщение «Ожидаемый тип данных
— число!».
"""
def plus_two(number):
    try:
        result = 2 + int(number)
        print(result)
    except ValueError:
        print("Ожидаемый тип данных — число!")

try:
    input_number = input("Введите число: ")
    plus_two(input_number)
except:
    print(f"Произошла ошибка:")