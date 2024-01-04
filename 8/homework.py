"""
1. Дан список целых чисел. Отсортируйте его в порядке не убывания значений. Выведите
полученный список на экран.
Решите эту задачу при помощи алгоритма сортировки вставкой. Решение оформите в
виде функцииInsertionSort(A).
В этой задаче нельзя п
"""
# #1.1 task
list=[]
len=5
 
for i in range(0, len):
    ele = int(input())
    list.append(ele)  
def InsertionSort(list):
	for i in range(1, len):
		key = list[i]
		j = i-1
		while j >= 0 and key < list[j]:
			list[j+1] = list[j]
			j -= 1
		list[j+1] = key
	return list

print(InsertionSort(list))


"""
Дан список целых чисел. Выведите все элементы этого списка в порядке не возрастания
значений. Выведите новый список на экран.
Решите эту задачу при помощи алгоритма сортировки выбором. Решение оформите в
виде функции SelectionSort(A).
В алгоритме сортировки выбором мы находим наибольший элемент в списке и ставим его
на первое место, затем находим наибольший элемент из оставшихся и ставим его на второе
место и т.д.
"""
#1.2 task
Arr = []
for i in range(0, len):
    ele = int(input())
    Arr.append(ele)  
def selection_sort_descending(arr):
    n = len
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr
print(selection_sort_descending(Arr))


"""
1. В супермаркете проводится беспрецедентная акция – «Покупая два любых товара,
третий получаешь бесплатно*», а внизу мелким шрифтом приписано «* - из трех выбранных
вами товаров оплачиваются два наиболее дорогих».
Вася, идя в супермаркет, определился, какие товары он хочет купить, и узнал, сколько
они стоят. Помогите ему определить минимальную сумму денег, которую ему нужно взять с
собой, чтобы в итоге стать счастливым обладателем этих товаров.
Программа получает на вход число N (1≤N≤1000), а затем N чисел – стоимости
выбранных Васей товаров. Все стоимости – натуральные числа, не превышающие 10000.
Выведите одно число – сумму денег, которую Вася должен взять с собой в супермаркет
(минимально возможную)
"""
#2.1 task
n=int(input())
array = []
for i in range(0, n):
    ele = int(input())
    array.append(ele)  
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def Sale(arr):
     summ=0
     for i in range(0, len(arr) - 1, 3):
          groupsum=arr[i+1]+arr[i+2]
          summ+=groupsum
     return summ
bubble_sort(array)
print(Sale(array))


"""
Дан список чисел (содержащий не менее двух элементов). Найдите в нем два
ближайших друг к другу числа (то есть два числа с наименьшей разностью).
Выведите эти числа в порядке не убывания.
"""
#2.2 task
arrayy = []
new = []
for i in range(0, 4):
    ele = int(input())
    arrayy.append(ele)
def KanyeWest(arr):
    if len(arr) >= 2:
        for i in range(0, len(arr) - 1, 2):
            det = abs(arr[i] - arr[i + 1])
            new.append(det + arr[i] / 10 + arr[i + 1] / 100)
        new.sort()
        number_str = str(new[0])
        dec = number_str.split('.')[-1]
        return int(dec[-2]), int(dec[-1])
    else:
        print("Error")

arrayy.sort()
result = KanyeWest(arrayy)
print(result)


"""
Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить к
элементам массива такой новый элемент, чтобы сумма элементов с положительными
значениями стала бы равна модулю суммы элементов с отрицательными значениями.
"""
#1.3 task
ar = []
positive_sum = 0
negative_sum = 0
ele=0
for i in range(0, 7):
    ele = int(input("Введите элементы массива(7): "))
    ar.append(ele)
for i in ar:
     if ar[i]>=0:
          positive_sum += ar[i]
     else:
          negative_sum += ar[i]
something = int(input())
while something+positive_sum == negative_sum:
    something = int(input())


"""
я не понял как использовать регулярные выражения :(
"""