def add(a, b):
    return a + b


def sub(a,  b):
    return a - b


operations = {
    "+": add,
    "-": sub

}


def get_data():

    op = input("Podaj rodz operacji +-")

    a = input("1 arg")
    b = input("2 arg")


    return op, int(a), int(b)


def kalkulator():
    op, a, b = get_data()
    
    result = operations[op](a, b)
           # add(a, b) jesli w op jest  +

    return result
    

def add(a, b, *args):
    return a + b + sum(args)


def sub(a,  b, *args):
    return a - b


operations = {
    "+": add,
    "-": sub

}


def get_data():

    op = input("Podaj rodz operacji +-")

    a = input("1 arg")
    b = input("2 arg")

    args = []

    while True:
        x = input("kolejna liczba lub k by zakonczyc")
        if x == "k":
            break
        args.append(int(x))
    return op, int(a), int(b), args


def kalkulator():
    op, a, b, args = get_data()
    
    result = operations[op](a, b, *args)
           # add(a, b) jesli w op jest  +

    return result