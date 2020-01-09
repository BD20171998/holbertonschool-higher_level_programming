from sys import stderr


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True

    except ValueError as err:
        stderr.write('{}'.format(err))
        print("Exception: {}".format(err), file=stderr)
        return False
