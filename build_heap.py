# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n =len(data)

    for i in range(n // 2 - 1, -1, -1):
        while True:
            maz = i 
            left = 2 * i + 1
            right = 2 * i + 2 if 2 * i + 2 < n else left
            if left < n and data[maz] > data [left]:
                maz = left

            if right < n and data[maz] > data[right]:
                maz = right

            if i != maz:
                data[i], data[maz] = data[maz], data[i]
                swaps.append((i, maz))
                i = maz
            else:
                break

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
