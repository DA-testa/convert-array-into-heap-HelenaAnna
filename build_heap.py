# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(1, len(data)):
        while i > 0 and data[(i -1 ) // 2] > data[i]:
            data[j], data[(i - 1) // 2] = data[(i - 1) // 2], data[i]
            swaps.append(((i - 1) // 2, i))
            i = (j - 1) // 2

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_type = input().strip().upper()

    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == "F":
        filename = input()
    
        with open(f"tests/{filename}") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
         
    else:
        print("Invalid input type", input_type)
        exit()
    
    # input from keyboard

    # checks if lenght of data is the same as the said lenght
    if len(data) != n:
        print(n)
        exit()

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    if len(swaps) >= 4 * n:
        print(4 * n)
        exit()

    print(len(swaps))

    # output all swaps

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
