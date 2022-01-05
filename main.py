# This is a simple calculator build script in python

def calc(operation=None, val1=None, val2=None):
    if val1 is None or val2 is None:
        while operation is None:
            operation = input("What kind of operation you want to perform?(+,-,*)")
    result = eval('{} {} {}'.format(val1, operation, val2))
    return result


def main():
    if calc('+', 1, 3) is not None:
        return "Build Successful!"
    else:
        return "Build Failed!"


if __name__ == "__main__":
    print(main())
