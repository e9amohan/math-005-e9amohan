"""python that returns the smallest positive number evenly divisible by between the range"""
def solver(p, q):
    """function for smallest positive number"""
    start = min(p, q)
    end = max(p, q)
    num = end

    while True:
        flag = True
        for i in range(start, end + 1):
            if num % i != 0:
                flag = False
                break
        if flag:
            return num
        num += 1


if __name__ == "__main__":
    print(solver(1, 10))
