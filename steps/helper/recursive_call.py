def hello(count):
    if count == 0:
        return 
    print("Hello, World!", count)

    count -=1
    hello(count)

if __name__ == '__main__':
    hello(5)