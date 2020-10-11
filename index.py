import sys
def main():
    print('Hello This is a demo commit for feature branch')

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print('Error: ', err)
        sys.exit(1)
