def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split()))
    ans = isSorted(arr, n)
    if ans:
        print("True")
    else:
        print("False")
