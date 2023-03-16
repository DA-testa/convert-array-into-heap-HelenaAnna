# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n // 2, -1, -1):
        swaps = uz_leju(data, i, n, swaps)

    for i in range (n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0,i))

        swaps = uz_leju(data, 0, i, swaps)

    return swaps

def uz_leju(data, i, n, swaps):
    while i * 2 +1 < n:
        j = i * 2 + 1

        if j + 1 < n and data[j + 1] > data[j]:
            j += 1

        if data[i] >= data[j]:
            break

        data[i], data[j] = data[j], data[i]
        swaps.append((i, j))

        i = j

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_type = input().strip().upper()

    if input_type == "I":
        n = int(input())
        data = input().split(" ")

    elif input_type == "F":
        filename = input()
    
        with open(f"tests/{filename}") as file:
            n = int(file.readline())
            data = file.readline().split(" ")
         
    else:
        print("Invalid input type", input_type)
        exit()
    
    # input from keyboard

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4 * n,
    print(len(swaps))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
