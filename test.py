# This is a simple calculator script in python

def calc(operation=None, val1=None, val2=None):
    if val1 is None or val2 is None:
        while operation is None:
            operation = input("What kind of operation you want to perform?(+,-,*)")
    result = eval('{} {} {}'.format(val1, operation, val2))
    return result


def test():
    if calc('-', 3, 1) != 2:
        return "Test Failed!"
    if calc('+', 3, 1) != 4:
        return "Test Failed!"
    if calc('*', 3, 1) != 3:
        return "Test Failed!"
    return "Test Passed!"


def main():
    return test()


if __name__ == "__main__":
    print(main())
