"""python that returns the smallest positive number evenly divisible by 10"""
from solver import solver
def answer(limit):
    """function for returning smallest +ve number"""
    return solver(1, limit)

if __name__ == "__main__":
    print(solver(1, 10))
