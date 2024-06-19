def heap(arr, n, i):
    max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[max] < arr[left]:
        max = left

    if right < n and arr[max] < arr[right]:
        max = right

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]

        heap(arr, n, max)

def hs(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)

def main():
    print("Enter numbers and type 'done' when finished:")

    arr = []
    while True:
        inp = input("Enter numbers and type 'done' when finished:")
        if inp.lower() == 'done':
            break
        try:
            num = float(inp)
            arr.append(num)
        except ValueError:
            print("eror! Please enter number or 'done' to finish.")

    if len(arr) == 0:
        print("No numbers to sort.")
    else:
        print(f"Original: {arr}")
        hs(arr)
        print(f"Sorted: {arr}")

if __name__ == "__main__":
    main()
