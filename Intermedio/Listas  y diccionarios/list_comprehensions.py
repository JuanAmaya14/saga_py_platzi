def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 10) if i % 3 != 0]

    print(squares)

    my_list = [1, 2, 3, 4, 5, 6, 7]

    elevate = [i for i in my_list if i != 5]

    print(elevate)


if __name__=='__main__':
    run()