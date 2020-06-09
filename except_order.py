

def wrong_usage():
    """
    Notice that the exception raised at line 14 will not be caught at line 15's except.
    Actually, the second exception was never called.
    :return:
    """
    try:
        print('Try')
        raise Exception('Raised in Try')
    except Exception as e:  # first
        print('First except')
        print(e)
        raise Exception('Raised in first except')
    except Exception as e:
        print('Second Except')
        print(e)
        print('Second got it!')


def right_usage():
    try:
        print('Try')
        raise Exception('Raised in Try')
    except Exception as e:  # first
        print('First except')
        print(e)
        try:
            print('    Inner try')
            raise Exception('    Raised in first except')
        except Exception as e:
            print('Second Except')
            print(e)
            print('Second got it!')


if __name__ == '__main__':
    right_usage()
    wrong_usage()
