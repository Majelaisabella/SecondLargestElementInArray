size = int(input())
if size <= 1:
    print("No second largest element present in the array")
else:
    numbers = []
    for _ in range(size):
        numbers.append(int(input()))
    
    largest = second = float('-inf')
    
    for current in numbers:
        if current > largest:
            second = largest
            largest = current
        elif current > second and current != largest:
            second = current
            
    print("No second largest element present in the array" if second == float('-inf') else second)
