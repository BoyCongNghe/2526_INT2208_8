def process_loan(age, income, credit, emp):
    # 1. Kiểm tra đầu vào không hợp lệ (Invalid Input)
    if not (18 <= age <= 65) or not (5.0 <= income <= 500.0) or not (300 <= credit <= 850) or emp not in ["C", "F"]:
        return "Invalid Input"

    # 2. Xử lý logic nghiệp vụ
    if credit <= 500:  
        return "REJECT"

    if income < 15.0:
        if credit > 700 and emp == "C": 
            return "MANUAL REVIEW"
        return "REJECT" 
        
    else:
        if emp == "C":
            return "APPROVE"
        return "MANUAL REVIEW"


# DANH SÁCH TEST CASE
# Dữ liệu dạng: (ID, age, income, credit, emp, Expected)
tests = [
    # Nhóm A
    ("A01", 17, 20.0, 700, "C", "Invalid Input"),
    ("A02", 18, 20.0, 700, "C", "APPROVE"),
    ("A03", 65, 20.0, 700, "C", "APPROVE"),
    ("A04", 66, 20.0, 700, "C", "Invalid Input"),
    ("A05", 30, 4.9,  700, "C", "Invalid Input"),
    ("A06", 30, 5.0,  750, "C", "MANUAL REVIEW"),
    ("A07", 30, 500.0, 750, "C", "APPROVE"),
    ("A08", 30, 500.1, 700, "C", "Invalid Input"),
    ("A09", 30, 20.0, 299, "C", "Invalid Input"),
    ("A10", 30, 20.0, 300, "C", "REJECT"),
    ("A11", 30, 20.0, 850, "C", "APPROVE"),
    ("A12", 30, 20.0, 851, "C", "Invalid Input"),
    ("A13", 30, 20.0, 700, "X", "Invalid Input"),
    
    # Nhóm B
    ("B01", 35, 10.0, 400, "C", "REJECT"),
    ("B02", 35, 50.0, 400, "F", "REJECT"),
    ("B03", 35, 30.0, 300, "C", "REJECT"),
    ("B04", 35, 30.0, 500, "F", "REJECT"),
    ("B05", 35, 10.0, 600, "C", "REJECT"),
    ("B06", 35, 10.0, 600, "F", "REJECT"),
    ("B07", 35, 10.0, 750, "F", "REJECT"),
    ("B08", 35, 10.0, 750, "C", "MANUAL REVIEW"),
    ("B09", 35, 20.0, 600, "C", "APPROVE"),
    ("B10", 35, 20.0, 750, "C", "APPROVE"),
    ("B11", 35, 20.0, 600, "F", "MANUAL REVIEW"),
    ("B12", 35, 20.0, 750, "F", "MANUAL REVIEW"),
    
    # Nhóm C
    ("C01", 40, 14.9, 750, "C", "MANUAL REVIEW"),
    ("C02", 40, 15.0, 750, "C", "APPROVE"),
    ("C03", 40, 20.0, 501, "C", "APPROVE"),
    ("C04", 40, 20.0, 700, "F", "MANUAL REVIEW"),
    ("C05", 40, 10.0, 701, "C", "MANUAL REVIEW")
]


# CHẠY TEST
for tc_id, age, income, credit, emp, expected in tests:
    actual = process_loan(age, income, credit, emp)
    
    if actual == expected:
        print(f"{tc_id}: PASS")
    else:
        print(f"{tc_id}: FAIL -> (Kỳ vọng: {expected}, Thực tế: {actual})")