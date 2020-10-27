def add(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = array[i][j]+1
def add_V2(array):
    new_array = []
    for i in range(len(array)):
        new_list = []
        for j in range(len(array[i])):
            new_list.append(array[i][j]+1)
        new_array.append(new_list)
    return new_array
def main():
    array = []
    print("""Input the array elements with spaces between columns.
One row per line, and an empty line at the end.""")
    while True:
        x = input()
        if x =="":
            break 
        else:
            List = []
            y = x.strip().split()
            for i in y:
                List.append(int(i))
            array.append(List)
    
    print("The array is:")
    print(array)    
    print("After executing the function add, the array is:")   
    add(array)
    print(array)
    print("A new array created with add_V2:")
    newest_array = add_V2(array)
    print(newest_array)
    print("After executing the function add_V2, the initial array is:")
    print(array)
main()
