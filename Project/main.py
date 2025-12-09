from quick_sort import quick_sort
from BubbleSort import bubble_sort

def main():
    print("=== Sorting Program ===")
    
    numbers = input("Enter numbers to sort (separated by space): ")
    arr = list(map(int, numbers.split()))

    print("Choose algorithm:")
    print("1 = quick sort")
    print("2 = bubble sort")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        result = quick_sort(arr)
        print("Result using Quick Sort:", result)
    elif choice == "2":
        result = bubble_sort(arr)
        print("Result using Bubble Sort:", result)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
