#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    print("{a} + {b} = {}".format(a, b, add(a, b)))
    print("{a} + {b} = {}".format(a, b, sub(a, b)))
    print("{a} + {b} = {}".format(a, b, mul(a, b)))
    print("{a} + {b} = {}".format(a, b, div(a, b)))
