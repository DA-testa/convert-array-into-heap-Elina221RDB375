def build_heap(info): 
    garums = len(info) 
    swaps = [] 
    for i in range(garums, -1, -1): 
        j = i 
        while True: 
            zars = j*2 + 1 
            if zars >= garums: 
                break 
            if zars+1 < garums and info[zars+1] < info[zars]: 
                zars = zars+1 
            if info[j] > info[zars]: 
                swaps.append((j, zars)) 
                info[j], info[zars] = info[zars], info[j] 
                j = zars 
            else: 
                break 
    return swaps 
 
 
def main(): 
    option = str(input()) 
    if "I" in option: 
        n = int(input()) 
        data = list(map(int, input().split())) 
        assert len(data) == n 
        swaps = build_heap(data) 
        print(len(swaps)) 
        for i, j in swaps: 
            print(i, j) 
        return 
    if "F" in option: 
        file = str(input()) 
        file = "tests/" + str(file) 
        with open(file, 'r') as pakete: 
            n = int(pakete.readline()) 
            data = list(map(int, pakete.readline().split())) 
        assert len(data) == n 
        swaps = build_heap(data) 
        print(len(swaps)) 
        return    
 
if name == "__main__": 
    main()
