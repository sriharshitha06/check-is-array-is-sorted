def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split()))
    print("True" if isSorted(arr, n) else "False")
