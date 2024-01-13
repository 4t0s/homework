start_one=[-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
result_one = [i**3 if i<0 else i**2 for i in start_one if i % 2==0]
print(result_one)


# start_two=['John','Kennedy','unknown']
# result_two = [len(i) for i in start_two]


# start_three=[-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
# result_three=[i**2 for i in start_three if i%2==0]
# print(result_three)


# start_three=[-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
# result_three=[i if i > 0 and i%5==0 else 0 for i in start_three]
# print(result_three)


# vowel='aeiouy'
# text = 'lorem ipsum'
# result_five=[i for i in text if i in vowel]
# print(result_five)


def decorator(func):
    def wrapper():
        result = func()
        result *= 2
        return result
    return wrapper
@decorator
def hello():
    return 'hello'
print(hello())