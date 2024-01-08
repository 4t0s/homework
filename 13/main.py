a=input()
b=input()
try:
    a=int(a)
    b=int(b)
    print(a+b)
except:
    a=str(a)
    b=str(b)
    print(a+b)


try:
    n = int(input())
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if n==0:
        raise ZeroDivisionError
    print(a + b + c)
except:
    print("Error")


try:
    coordinateX1 = int(input())
    coordinateY1 = int(input())
    coordinateX2 = int(input())
    coordinateY2 = int(input())
    coordinates = [coordinateX1, coordinateY1, coordinateX2, coordinateY2]
    for i in coordinates:
        if i > 8 or i < 1:
            raise ZeroDivisionError

    if coordinateX1 % 2 == 0 and coordinateY1 % 2 != 0:
        color1 = 'black'
    elif coordinateX1 % 2 == 0 and coordinateY1 % 2 == 0:
        color1 = 'white'
    elif coordinateX1 % 2 != 0 and coordinateY1 % 2 != 0:
        color1 = 'white'
    elif coordinateX1 % 2 != 0 and coordinateY1 % 2 == 0:
        color1 = 'black'
    if coordinateX2 % 2 == 0 and coordinateY2 % 2 != 0:
        color2 = 'black'
    elif coordinateX2 % 2 == 0 and coordinateY2 % 2 == 0:
        color2 = 'white'
    elif coordinateX2 % 2 != 0 and coordinateY2 % 2 != 0:
        color2 = 'white'
    elif coordinateX2 % 2 != 0 and coordinateY2 % 2 == 0:
        color2 = 'black'
    if color1 == color2:
        print("YES")
    else:
        print("NO")
except:
    print('Error')


try:
    ladyaCoordinateX = int(input())
    ladyaCoordinateY = int(input())
    otherCoordinateX = int(input())
    otherCoordinateY = int(input())
    coordinatess = [ladyaCoordinateY,ladyaCoordinateX,otherCoordinateY,otherCoordinateX]
    for i in coordinatess:
        if i > 8 or i < 1:
            raise ZeroDivisionError
    if ladyaCoordinateX == otherCoordinateX or ladyaCoordinateY == otherCoordinateY:
        print('YES')
    else:
        print('NO')
except:
    print('ERROR')
    
    
choice = int(input("Ваша фигура:\n [1]ладья\n [2]король\n"))
if choice == 2:
    try:
        crownCoordinateX = int(input())
        crownCoordinateY = int(input())
        otherCoordinateX = int(input())
        otherCoordinateY = int(input())
        coordinatess = [crownCoordinateY,crownCoordinateX,otherCoordinateY,otherCoordinateX]
        for i in coordinatess:
            if i > 8 or i < 1:
               raise ZeroDivisionError
        if crownCoordinateX == otherCoordinateX+1 or crownCoordinateX == otherCoordinateX-1 or crownCoordinateY == otherCoordinateY+1 or crownCoordinateY == otherCoordinateY-1:
           print('YES')
        elif crownCoordinateX == otherCoordinateX+1 and crownCoordinateX == otherCoordinateY-1 or crownCoordinateX == otherCoordinateX-1 and crownCoordinateX == otherCoordinateY+1 or crownCoordinateX == otherCoordinateX+1 and crownCoordinateX == otherCoordinateY+1 or crownCoordinateX == otherCoordinateX-1 and crownCoordinateX == otherCoordinateY-1:
          print('YES')
        else:
           print('NO')
    except:
       print('ERROR')
elif choice == 1:
    try:
        ladyaCoordinateX = int(input())
        ladyaCoordinateY = int(input())
        otherCoordinateX = int(input())
        otherCoordinateY = int(input())
        coordinatess = [ladyaCoordinateY,ladyaCoordinateX,otherCoordinateY,otherCoordinateX]
        for i in coordinatess:
            if i > 8 or i < 1:
                raise ZeroDivisionError
        if ladyaCoordinateX == otherCoordinateX or ladyaCoordinateY == otherCoordinateY:
            print('YES')
        else:
            print('NO')
    except:
        print('ERROR')


