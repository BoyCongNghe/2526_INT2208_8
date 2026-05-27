# 1. HÀM XỬ LÝ LOGIC
def kiem_tra_tam_giac(a, b, c):
    if a < 1 or b < 1 or c < 1 or a > 100 or b > 100 or c > 100:
        return "Invalid Input"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
        
    return "Scalene"   


# 2. DANH SÁCH 18 TEST CASE
# Cấu trúc mỗi dòng: [Cạnh a, Cạnh b, Cạnh c, Expected Result]
danh_sach_test = [
    # Nhóm 1: Đầu vào vi phạm
    [0, 5, 5, "Invalid Input"],
    [5, -1, 5, "Invalid Input"],
    [5, 5, 101, "Invalid Input"],
    [0, 0, 0, "Invalid Input"],
    
    # Nhóm 2: Không phải tam giác
    [1, 2, 3, "Not a Triangle"],
    [1, 1, 10, "Not a Triangle"],
    [10, 2, 3, "Not a Triangle"],
    [2, 10, 3, "Not a Triangle"],
    
    # Nhóm 3: Tam giác đều
    [1, 1, 1, "Equilateral"],
    [50, 50, 50, "Equilateral"],
    [100, 100, 100, "Equilateral"],
    
    # Nhóm 4: Tam giác cân
    [5, 5, 8, "Isosceles"],
    [8, 5, 5, "Isosceles"],
    [5, 8, 5, "Isosceles"],
    [100, 100, 99, "Isosceles"],
    [1, 2, 2, "Isosceles"],
    
    # Nhóm 5: Tam giác thường
    [3, 4, 5, "Scalene"],
    [98, 99, 100, "Scalene"]
]


# 3. VÒNG LẶP CHẠY TEST
for thu_tu, test_case in enumerate(danh_sach_test, start=1):
    a, b, c, mong_doi = test_case
    thuc_te = kiem_tra_tam_giac(a, b, c)
    if thuc_te == mong_doi:
        print(f" TC{thu_tu:02d} - Input({a}, {b}, {c}) -> Pass")
    else:
        print(f"TC{thu_tu:02d} - Input({a}, {b}, {c}) -> FAIL")
        print(f"   + Mong đợi : {mong_doi}")
        print(f"   + Thực tế  : {thuc_te}")