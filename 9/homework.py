start_one=[1,2,3,4,5,6,7]
new_one = [None if i % 2==0 else i*1 for i in start_one]
result_one = [k * (k**2) if k is not None else None for k in new_one]
resultt_one = dict.fromkeys(new_one, 0)
for k, value in zip(new_one, result_one):
    resultt_one[k] = value
filtered_one = {k: v for k, v in resultt_one.items() if k is not None}
print(filtered_one)


start_two = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] 
result_two = set(start_two)
resultt_two = [None if i % 2!=0 else i*1 for i in result_two ]
filtered_two = {i for i in resultt_two if i is not None}
print(filtered_two)


result_three = [i*10 for i in range(10)]
print(result_three)


def numbers_divisible_by_seven(n):
    for number in range(n + 1):
        if number % 7 == 0:
            yield number
n = int(input())
for num in numbers_divisible_by_seven(n):
    print(num)
    

#я не знаю как сделать последнее