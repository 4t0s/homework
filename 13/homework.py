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
except Exception as e:
    print(f"An error: {e}")
