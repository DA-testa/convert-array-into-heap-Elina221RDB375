# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    dataSorted = sorted(data)
    lenSorted = len(dataSorted)

    def isMinHeap():
        for i in range(0, len(data)-3):
            if data[i] > data[i+1] and data[i] > data[i+2]:
                return False

        return True

    def parent(minIndex):
        if minIndex > 2:
            if minIndex % 2 == 0:
                parentIndex = int((minIndex - 2) / 2)
            else:
                parentIndex = int((minIndex - 1) / 2)
        else:
            return 0
        
        return parentIndex

    def swap(parentIndex, minIndex):
        swaps.append([parentIndex, minIndex])

        temp = data[minIndex]
        data[minIndex] = data[parentIndex]
        data[parentIndex] = temp

    count = 0
    while not isMinHeap():
        minValue = dataSorted[count] # min(data) nextmin?
        minIndex = data.index(minValue)

        parentIndex = parent(minIndex)

        while data[parentIndex] > data[minIndex]:
            swap(parentIndex, minIndex)
            
            minIndex = data.index(minValue)
            parentIndex = parent(minIndex)

        count+=1
        if(count>lenSorted-1):
            break

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    switch = input()
    if "F" in switch:
        filename = input()
        if filename != "a":
            f = open("./tests/"+filename, "r")
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            f.close()
    elif "I" in switch:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
