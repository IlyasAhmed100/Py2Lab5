import time

start = time.time()

with open("list.txt", "r") as data:
    listData = data.readlines()
    listSplit = []
    for spaces in listData:
        listSplit.append(spaces.split(" "))
    listSplit[0].remove('')
    listInteger = [int(elements) for elements in listSplit[0]]
    


def search_linear(A, x):
    i = 0
    while i < len(A):
        if A[i] == x:
            return i
        i = i + 1
    return -1



def search_binary(A, x):
    lower = 0
    upper = len(A) - 1
    while lower <= upper:
        mid = (upper + lower) // 2
        if A[mid] == x:
            return mid
        else:
            if A[mid] < x:
                lower = mid + 1
            else:
                upper = mid - 1
    return -1

def main():
    whichSearch = input("Would you like to be a linear or binary search on the list. " + "Type 'l' for linear and 'b' for binary." + '\n').lower()
    x = int(input('\n' + "What number would you like to search for?" + '\n'))
    if whichSearch == "l":
        return search_linear(listInteger, x)
    elif whichSearch == "b":
        return search_binary(listInteger, x)
    else:
        return "This isn't a valid input"


#print(listInteger)
print(main())


end = time.time()
timeTaken = end - start
print("Time taken for your code to run is: " + str(timeTaken))
