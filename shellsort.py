#!/usr/bin/env python3


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    change = 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                print(f"{change}. `{arr}`")
                change += 1
                arr[j] = arr[j - gap]
                j -= gap
            print(f"{change}. `{arr}`")
            change += 1
            arr[j] = temp
        gap //= 2

    return arr


if __name__ == '__main__':
    arr = [ 80, 57, 65, 30, 45, 77, 27, 4, 90, 54, 45, 2, 63, 38, 81, 28, 62 ]
    arr = shell_sort(arr)
    print(f"`{arr}`")