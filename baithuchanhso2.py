def pascal_triangle(n):
    if n <= 0:
        print("Invalid input. n must be a positive integer.")
        return
    
    # Tạo một ma trận để lưu giá trị của tam giác Pascal
    pascal = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Khởi tạo giá trị cho tam giác Pascal
    for i in range(n + 1):
        pascal[i][0] = 1
        pascal[i][i] = 1
    
    # Tính các giá trị còn lại
    for i in range(2, n + 1):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    
    # In tam giác Pascal
    for i in range(n + 1):
        print("n={}".format(i), end=" ")
        for j in range(i + 1):
            print(pascal[i][j], end=" ")
        print()

# Test
n = int(input("Nhập vào số nguyên dương n: "))
pascal_triangle(n)
